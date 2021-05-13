n, m = map(int, input().split())
x = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    x[b] = max(x[b], a)
ans = 0
bmx = 0
for i in range(n+1):
    if bmx <= x[i]:
        ans += 1
        bmx = i
print(ans)