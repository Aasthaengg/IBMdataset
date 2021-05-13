from itertools import combinations
n=int(input())
dp=[0]*5
for i in range(n):
  s=input()
  if s[0]=="M":dp[0]+=1
  if s[0]=="A":dp[1]+=1
  if s[0]=="R":dp[2]+=1
  if s[0]=="C":dp[3]+=1
  if s[0]=="H":dp[4]+=1
ans=0
for a,b,c in combinations(dp,3):
  ans+=a*b*c
print(ans)