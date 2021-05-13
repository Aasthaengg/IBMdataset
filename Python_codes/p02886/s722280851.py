N=int(input())
d=list(map(int,input().split()))
res=[0]*N
for i in range(N):
  for j in range(N):
    if(i!=j):
      res[i]+=d[i]*d[j]
print(int(sum(res)/2))