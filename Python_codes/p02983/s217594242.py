L, R = map(int, input().split())

if R - L >= 2019:
    res = 0
else:
    res = float("inf")
    L = L % 2019
    R = R % 2019
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            res = min(res, (i * j) % 2019)
print(res)
