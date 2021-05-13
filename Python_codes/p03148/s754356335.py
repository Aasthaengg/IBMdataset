import heapq
from collections import deque
n,k=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
  l[i].reverse()
  l[i][0]*=-1
heapq.heapify(l)

check=[0 for i in range(10**5+1)]
L=[]
L2=[]
L2=deque(L2)
ans=[]

for i in range(k):
  x=heapq.heappop(l)
  if check[x[1]]==0:
    L.append(-x[0])
    check[x[1]]=1
  else:
    L2.append(-x[0])
p=sum(check)
ans.append(sum(L)+sum(L2)+p**2)

y=n-k
while y!=0:
  x=heapq.heappop(l)
  if check[x[1]]==0:
    L.append(-x[0])
    check[x[1]]=1
    if len(L2)==0:
      break
    z=L2.pop()
    p+=1
    ans.append(ans[-1]-(p-1)**2-x[0]-z+p**2)
  y-=1

print(max(ans))