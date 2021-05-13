n,t=map(int,input().split())
ans=1000000
for i in range(n):
  x,y=map(int,input().split())
  if y<=t:
    ans=min(ans,x)
if ans<=100000:
  print(ans)
else:
  print("TLE")