n,t = map(int,input().split())
c = [ list(map(int,input().split())) for _ in range(n) ]

ans = 1001
for i,j in c:
  if j <= t:
    ans = min(ans,i)

print('TLE' if ans == 1001 else ans)
