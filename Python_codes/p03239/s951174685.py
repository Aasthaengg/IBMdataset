n,t = map(int,input().split())

ans = 10**9

for i in range(n):
  c,y = map(int,input().split())
  if y<=t:
    ans = min(ans,c)
    
if ans == 10**9:
  print("TLE")
else:
  print(ans)
