n = int(input())

f = [[] for _ in range(n)]
a = [[] for _ in range(n)]

for i in range(n):
    f[i] = list(map(int, input().split()))

for i in range(n):
    a[i] = list(map(int, input().split()))

ans = -float("inf")
for times in range(1, 1 << 10):
    profit = 0
    for i in range(n):
        cnt = 0
        for j in range(10):
            if times >> j & 1 and f[i][j]:
                cnt += 1
        profit += a[i][cnt]

    ans = max(ans, profit)

print(ans)
