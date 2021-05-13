n,m=map(int,input().split())
dp=[0]*(n+1)
charge=[0]*(n+1)
cnt=0
ans=0
for i in range(m):
  q=input()
  if dp[int(q[:-3])]!="A" and q[-2]=="W":
    dp[int(q[:-3])]="W"
    charge[int(q[:-3])]+=1
  elif dp[int(q[:-3])]!="A" and q[-2]=="A":
    dp[int(q[:-3])]="A"
    ans+=1
    cnt+=charge[int(q[:-3])]
    charge[int(q[:-3])]=0
print(ans,cnt)