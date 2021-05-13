import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
tree=[[] for i in range(n+1)]
for i in range(n-1):
    a,b,c=mp()
    tree[a].append((b,c))
    tree[b].append((a,c))
q,k=mp()
dist=[-1]*(n+1)
dist[k]=0
deq=deque()
deq.append(k)

while len(deq):
    p=deq.popleft()
    for x,y in tree[p]:
        if dist[x]==-1:
            dist[x]=dist[p]+y
            deq.append(x)
for i in range(q):
    xi,yi=mp()
    print(dist[xi]+dist[yi])