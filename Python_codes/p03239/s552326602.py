N,T=list(map(int,input().split()))
minCos = 10000
ans = 0
for i in range(N):
  c,t=list(map(int,input().split()))
  if t <= T:
    if min(minCos,c) == c:
      ans = c
      minCos = c
if ans == 0:
  print("TLE")
else:
  print(ans)