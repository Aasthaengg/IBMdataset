import sys 
sys.setrecursionlimit(10**6)
N=int(input())
A=[[]for i in range(N)]
X=[list(map(int, input().split())) for _ in range(N-1)]
for i in range(N-1):
  a=X[i][0]
  b=X[i][1]
  a-=1
  b-=1
  A[a].append(b)
  A[b].append(a)
D=list(map(int, input().split()))
D=sorted(D)[::-1]
from collections import deque
d=deque(D)
E=[-1]*N
def f(now,pre):
  for i in A[now]:
    if i!=pre and E[i]==-1:
      E[i]=d.popleft()
      f(i,now)
E[0]=d.popleft()
f(0,0)
print(sum(D[1:]))
print(*E)
