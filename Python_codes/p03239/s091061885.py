n, T = map(int, input().split())
ans = 1001
ok = False
for i in range(n):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
        ok = True
if ok:
    print(ans)
else:
    print('TLE')
