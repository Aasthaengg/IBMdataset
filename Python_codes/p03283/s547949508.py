import itertools

n,m,q=map(int,input().split()) #0-indexed

LR=[[0]*(n+1) for i in range(n+1)]

for i in range(m):
  l,r=map(int,input().split())
  LR[l][r]+=1

for i in range(n):
  LR[i]=list(itertools.accumulate(LR[i]))


for i in range(q):
  l,r=map(int,input().split())
  ans=0
  for j in range(l,r+1):
    ans+=LR[j][r]-LR[j][l-1]

  print(ans)