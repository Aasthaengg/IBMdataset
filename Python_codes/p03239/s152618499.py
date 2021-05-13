N,T = map(int,input().split())
ct = [list(map(int,input().split())) for _ in range(N)]

ct.sort(key=lambda x: x[1])
ans = 10**18

for c,t in ct:
  if t > T:
    break
  ans = min(ans,c)
if ans == 10**18:
  ans = 'TLE'
print(ans)