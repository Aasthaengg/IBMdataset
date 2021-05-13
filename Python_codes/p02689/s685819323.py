n, m = map(int, input().split())
h = list(map(int, input().split()))
res = [0] * n

"""
0: 初期値
1: highest
-1: not highest
"""
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if h[a] > h[b]:
        if res[a] == 0:
            res[a] = 1
        res[b] = -1
    elif h[a] < h[b]:
        res[a] = -1
        if res[b] == 0:
            res[b] = 1
    elif h[a] == h[b]:
        res[a] = -1
        res[b] = -1

print(res.count(1) + res.count(0))