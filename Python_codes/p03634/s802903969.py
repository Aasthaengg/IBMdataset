from collections import deque
import sys
INF = 11414191981036436433-4

n = int(input())
g = [[] for i in range(n)]
for v in range(n-1):
    a,b,c = map(int,input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))
    
q,k = map(int,input().split())
k -= 1

r = [INF]*n
que = deque([k])
r[k] = 0
while que:
    v = que.popleft()
    rr = r[v]
    for w,x in g[v]:
        if r[w] == INF:
            r[w] = rr + x
            que.append(w)
            
for i in range(q):
    d,e = map(int,input().split())
    print(r[d-1] + r[e-1])