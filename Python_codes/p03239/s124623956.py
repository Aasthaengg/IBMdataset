n,T = map(int,input().split())
ct = [map(int, input().split()) for _ in range(n)]
c,t = [list(i) for i in zip(*ct)]
ans = 1000000
for i in range(n):
  if(T >= t[i]):
    ans = min(ans,c[i])
if(ans == 1000000):
  print('TLE')
else:
  print(ans)