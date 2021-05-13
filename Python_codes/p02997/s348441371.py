from itertools import combinations
n,k=map(int,input().split())
x=(n-1)*(n-2)//2
if k>x:
  print(-1)
  exit()
ans=[]
for i in range(2,n+1):
  ans.append((1,i))
if k<x:
  cnt=x-k
  for i,j in combinations(range(2,n+1),2):
    if cnt>0:
      ans.append((i,j))
      cnt-=1
    else:
      break
print(len(ans))
for arr in ans:
  print(*arr)