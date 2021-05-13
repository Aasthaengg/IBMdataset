import sys
read = sys.stdin.readline


# 下の桁から貪欲に見ていくと解ける
# 1の位が4以下ならそのまま紙幣で支払うのが得→自身をそのまま答えに採用 (枚数として加算)
# 6以上ならばお釣り狙いのほうが得→自身は0にセットして、上位桁を+1する (枚数として10-自身を加算)
# 5ちょうどのときは、お釣りもそのまま払っても枚数は変わらない。だけど555みたいに、上位桁に+1すると得になる可能性がある。
# 555→15枚, 1000-445→15枚
# つまり5が出たときは更に上位の桁を見て、4以下ならそのまま払うほうが得,5以上なら桁上りのほうが得

# 5ちょうどのときは？ #お釣りもそのまま払っても同じ。だけど上位 お釣り狙いだと上の桁が多くなって支払う金額が増える可能性がある？
# 5ピッタリのときに上位桁に+1すると悪くなる場合が存在する 455 とは 15にってしまう
# 5ピッタリのときはどうするのがよいのか？

N = '00' + read()[:-1]

N = N[::-1]
ans = 0
# agari = 0
# is_pre5 = False
# for n in N:
#     n = int(n) + agari
#     print(n, ans)
#     if is_pre5:
#         if n == 5:
#             ans += n
#             continue

#         if n < 5:
#             # そのまま支払う
#             ans += n
#             agari = 0
#         else:
#             # 桁上り
#             ans += 9 - n
#             agari = 1
#     else:
#         if n == 5:
#             is_pre5 = True
#             ans += n
#             agari = 0
#             # もし5だったら5が終わるまでなめる
#         elif n < 5:
#             ans += n
#             agari = 0
#         else:
#             ans += 10 - n
#             agari = 1
#     if n != 5:
#         is_pre5 = False

i = 0
lo = int(N[i])
while i < len(N) - 1:
    hi = int(N[i + 1])
    # print(hi, lo, i)
    if lo == 5 and hi == 5:
        # 5が連続してた場合
        # 5の最後まで移動(移動の道中は 5+4+4...としていく)
        # 5じゃなくなったhiに対して足し算する必要がある。
        ans += 5
        i += 1
        while i < len(N) - 1 and N[i + 1] == '5':
            ans += 4
            # print(i)
            i += 1
        ans += 4
        # low = N[i]
        hi = int(N[i + 1]) + 1
        # print(hi, lo, i)

        # loが5以外のとき (お釣りが良いか、そのまま払うのが良いか考えるだけ)
    elif lo == 5:
        ans += lo
        if hi < 5:
            pass
        else:
            hi += 1
    elif lo < 5:  # 5が連続しないときもここに入る
        ans += lo
    else:
        ans += 10 - lo
        hi += 1  # 上の桁が繰り上がる
    lo = hi  # 桁を一つずらす
    i += 1


print(ans)
