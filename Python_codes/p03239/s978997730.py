N, T = map(int, input().split())
ans = 10**5
for i in range(N):
    a, b = map(int, input().split())
    if b <= T:
        ans = min(ans, a)
if ans is 10**5: print('TLE')
else: print(ans)
