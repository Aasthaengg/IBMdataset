dp=[0]*4
for i in range(3):
  a,b=map(int,input().split())
  dp[a-1]+=1
  dp[b-1]+=1
if dp.count(3)==1 or dp.count(0)==1:
  print("NO")
else:
  print("YES")