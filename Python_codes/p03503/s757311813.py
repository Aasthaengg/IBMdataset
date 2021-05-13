n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

res = -float('inf')
for i in range(1, 2 ** 10):
    profit = 0
    for j in range(n):
        cnt = 0
        for k in range(10):
            if (i >> (9 - k)) & 1 and f[j][k]:
                cnt += 1
        profit += p[j][cnt]
    res = max(res, profit)

print(res)