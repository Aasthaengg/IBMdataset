n,m=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
p=[0]*m
for s in S:
  k=0
  d=[0]*(m+1)
  for i in range(m):
    if T[i]==s:
      k+=p[i-1]+1
    d[i]=(p[i]+k)%(10**9+7)
  p=d
print(p[-2]+1)