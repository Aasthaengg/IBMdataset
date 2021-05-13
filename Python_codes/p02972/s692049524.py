n=int(input())
a=[0]+list(map(int,input().split()))
d=[[] for _ in range(n+1)]
p=[0]*(n+1)
for i in range(1,n+1):
  for j in range(i,n+1,i):
    d[j]+=[i]
ans=[]
for i in range(n,0,-1):
  if a[i]!=p[i]:
    ans+=[i]
    for j in d[i]:
      p[j]=1-p[j]
  else:p[i]=0
print(len(ans))
print(*ans)