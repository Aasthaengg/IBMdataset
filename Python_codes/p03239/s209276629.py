n, T = map(int, input().split())
ans = float('inf')
f = False
for i in range(n):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
        f = True
if f:
    print(ans)
else:
    print('TLE')
