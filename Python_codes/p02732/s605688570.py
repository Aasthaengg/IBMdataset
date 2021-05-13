N=int(input())
A=list(map(int,input().split()))
d=dict([])
ans=0
for a in A:
  if a in d:
    ans+=d[a]
    d[a]+=1
  else:
    d[a]=1
for a in A:
  print(ans-d[a]+1)