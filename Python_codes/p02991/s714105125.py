#### 132_E

import queue
import sys
sys.setrecursionlimit(300000)
 
n,m=map(int,input().split())

edges=[[] for i in range(3*n)]
for _ in range(m):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    u0,u1,u2=u,u+n,u+2*n
    v0,v1,v2=v,v+n,v+2*n
    edges[u0].append(v1)
    edges[u1].append(v2)
    edges[u2].append(v0)
    
s,t=map(int,input().split())
s,t=s-1,t-1
    
def bfs(s,t):
    que=queue.Queue()
    que.put(s)
    d[s]=0
    visit[s]=True
    while not que.empty():
        q=que.get()
        if q==t:
            return d[t]
        for z in edges[q]:
            if visit[z]==False:
                que.put(z)
                d[z]=d[q]+1
                visit[z]=True
    return d[t]
                
visit=[False for _ in range(3*n)]
d=[-1 for _ in range(3*n)]

print(bfs(s,t)//3)