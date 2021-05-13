n, m, c = map(int, input().strip().split())
b = list(map(int, input().strip().split()))
a = [list(map(int, input().strip().split())) for _ in range(n)]

res = 0
for i in range(n):
    sum = c
    for j in range(m):
        sum += a[i][j] * b[j]
    if sum > 0:
        res += 1

print(res)
