n, T = list(map(int, input().split()))
ans = 1001
for _ in range(n):
    c, t = list(map(int, input().split()))
    if t <= T:
        ans = min(ans, c)
if ans == 1001:
    print('TLE')
else:
    print(ans)