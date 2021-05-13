n=int(input())
G=[]
for i in range(n):
    u,k,*l=map(int,input().split())
    G.append(l)
#print(G)

#BFS
from collections import deque
def bfs(G,v,p):
    que=deque()
    que.append((v,p))
    log=[-1]*n
    log[0]=0
    while que:
        #queの先頭を取り出す
        V,P=que.popleft()
        for next_v in G[V-1]:
            if log[next_v-1]!=-1:continue
            log[next_v-1]=log[V-1]+1
            que.append((next_v,V))
    return log

log=bfs(G,1,-1)
for i in enumerate(log,1):
    print(*i)
