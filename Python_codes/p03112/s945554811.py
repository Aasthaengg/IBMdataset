import bisect
A, B, Q = map(int, input().split())
INF = 10 ** 18
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

for q in range(Q):
    x = int(input())
    y1 = bisect.bisect_right(s, x)
    y2 = bisect.bisect_right(t, x)
    res = INF
    # 最も近い神社の候補２つ
    for sx in [s[y1 - 1], s[y1]]:
        # 最も近い寺の候補２つ
        for tx in [t[y2 - 1], t[y2]]:
            # 神社、寺の順で訪れる場合
            d1 = abs(sx - x) + abs(tx - sx)
            # 寺、神社の順で訪れる場合
            d2 = abs(tx - x) + abs(sx - tx)
            res = min(res, d1, d2)
    print(res)
