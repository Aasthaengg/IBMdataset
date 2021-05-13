import sys
input = sys.stdin.buffer.readline
n,q=map(int,input().split())
import heapq
S=[]
D=dict()
for i in range(n):
  s,t,x=map(int,input().split())
  S.append((1,x,max(0,s-x)))
  S.append((-1,x,max(0,t-x)))
  D[x]=False
S.sort(key=lambda x:x[2])
X=[]
cur=0
for i in range(q):
  d=int(input())
  while cur<2*n:
    a,b,c=S[cur]
    if c>d:
      break
    else:
      cur+=1
      if a==1:
        heapq.heappush(X,b)
        D[b]=True
      else:
        D[b]=False
  while X:
    ans=heapq.heappop(X)
    if D[ans]:
      print(ans)
      heapq.heappush(X,ans)
      break
  if not X:
    print(-1)
