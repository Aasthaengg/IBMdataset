def e_roadwork(N, Q, Construction, D):
    from bisect import bisect_left
    from operator import itemgetter
    ans = [-1] * Q
    skip = [-1] * Q

    Construction.sort(key=itemgetter(2))

    for s, t, x in Construction:
        l = bisect_left(D, s - x)
        r = bisect_left(D, t - x)
        t = l
        while t < r:
            if skip[t] == -1:
                ans[t] = x  # lからr-1の時刻に出発した人は座標xの工事に引っかかる
                skip[t] = r  # lからr-1の時刻に出発した人はもう調べないようにする
                t += 1
            else:
                t = skip[t]  # tが指定する人はもう調べ終わっているので飛ばす
    return ' '.join(map(str, ans))
    # 参考: https://atcoder.jp/contests/abc128/submissions/5654623

N, Q = [int(i) for i in input().split()]
Construction = [tuple(int(i) for i in input().split()) for j in range(N)]
D = [int(input()) for _ in range(Q)]
print(e_roadwork(N, Q, Construction, D))