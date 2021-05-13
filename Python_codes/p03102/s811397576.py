n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = 0

for i in range(n):
    zzz = 0
    for j in range(m):
        zzz += a[i][j] * b[j]
    if zzz > -c:
        ans += 1

print(ans)
