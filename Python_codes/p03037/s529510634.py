n, m = map(int, input().split())

g = [0] * (n+2)
for i in range(m):
    l,r = map(int,input().split())
    g[l] += 1
    g[r+1] -= 1

now = 0
ans = 0
for i in range(1, n+1):
    now += g[i]
    if now >= m:
        ans += 1

print(ans)
