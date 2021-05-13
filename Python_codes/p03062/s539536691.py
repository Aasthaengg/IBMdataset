N = int(input())
A = list(map(int, input().split()))

# 絶対値の和
plus_sum = 0
# 負の数の個数
minus_num = 0
# 絶対値が最も小さい数
min_abs = 10**10

for a in A:
    plus_sum += abs(a)
    if a < 0:
        minus_num += 1
    if abs(a) < abs(min_abs):
        min_abs = a

# 0が入っていたら全部正にできる
if 0 in A:
    print(plus_sum)

else:
    # 0が含まれない場合、負の個数の偶奇で場合分け
    # 偶数個なら全部正にできる
    if minus_num % 2 == 0:
        print(plus_sum)

    # min_absだけマイナス、他はプラス
    elif minus_num % 2 == 1:
        ans = plus_sum - 2 * abs(min_abs)
        print(ans)
