import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
T = [[] for _ in range(n)]
for i in range(n-1):
    ai,bi = map(int, input().split( ))
    ai-=1;bi-=1
    T[ai].append(bi)
    T[bi].append(ai)

c = list(map(int, input().split( )))
c.sort()


#最小の数字は葉に書き込む
#次点は葉あるいは最小頂点除いたら葉な点
#r = 0
Q = deque()
Q.append(0)
P = [-1 for i in range(n)]
P[0] = 0
D = [0]*n
L=[]
while Q:
    v = Q.popleft()
    leaf = True
    for u in T[v]:
        if P[u]<0:
            D[v]+=1
            P[u]=v
            leaf = False
            Q.append(u)
    if leaf:
        L.append(v)

Q =deque(L)

j = 0
A = [0]*n
m = 0
while Q:
    v = Q.popleft()
    A[v] = c[j]
    if v:
        m+=c[j]
    j+=1
    D[P[v]]-=1
    if not D[P[v]] and v:
        Q.append(P[v])
print(m)
print(*A)
