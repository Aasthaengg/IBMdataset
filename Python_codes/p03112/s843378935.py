a, b, q = map(int, input().split())
INF = 10 ** 15
s = [-INF] + [int(input()) for _ in range(a)] + [INF] # sorted
t = [-INF] + [int(input()) for _ in range(b)] + [INF] # sorted

from bisect import bisect_left, bisect_right

for _ in range(q):
    x = int(input())
    i = bisect_left(s, x)
    j = bisect_left(t, x)
    d = INF
    for sx in [s[i - 1], s[i]]:
        for tx in [t[j - 1], t[j]]:
            d1 = abs(sx - x) + abs(sx - tx)
            d2 = abs(tx - x) + abs(sx - tx)
            d = min(d, d1, d2)
    print(d)