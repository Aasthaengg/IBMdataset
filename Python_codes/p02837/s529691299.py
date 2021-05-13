import itertools
N=int(input())
A=[]
for i in range(N):
  a=[]
  B=int(input())
  for _ in range(B):
    x,y=map(int,input().split())
    a.append([x,y])
  A.append(a)
ans=0
for i in list(itertools.product(range(2),repeat=N)):
  for j in range(len(A)):
    flag=True
    if i[j]==0:
      continue
    for x,y in A[j]:
      if i[x-1]!=y:
        flag=False
        break
    if not flag:
      break
  if flag:
    ans=max(ans,sum(i))
print(ans)