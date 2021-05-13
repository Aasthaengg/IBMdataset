N,Q = list(map(int,input().split()))
ad={}
point={}
P = {}
color={}
child={}

for n in range(N):
    ad[n+1]=set()
    child[n+1]=set()
    color[n+1] = -1
    point[n+1] = 0
    P[n+1] = 0

for n in range(N-1):
    a,b = list(map(int,input().split()))
    ad[a].add(b)
    ad[b].add(a)
    
for q in range(Q):
    p,x = list(map(int,input().split()))
    point[p] += x

#BFS
from collections import deque
start=1
visit = []
que = deque([start])

i=0
while len(que) > 0:
    start = que.popleft()
    color[start] = 1
    
    for v in ad[start]:
        if color[v] == -1:
            que.append(v) 
            color[v] = 0
            point[v] += point[start]
    
#     print(que,point)
ans=' '.join(map(str,point.values()))
print(ans)