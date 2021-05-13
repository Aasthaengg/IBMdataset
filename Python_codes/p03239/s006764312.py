n,t = map(int,input().split())
ans = 100000
for i in range(n):
    a,b = map(int,input().split())
    if b <= t: ans = min(ans,a)
if ans == 100000: print('TLE')
else: print(ans)