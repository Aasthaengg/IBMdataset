n, T = map(int, input().split())
ans = float('inf')
for _ in range(n):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
print('TLE' if ans == float('inf') else ans)