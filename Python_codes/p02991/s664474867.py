N,M = map(int,input().split())
import time
start_t = time.time()
path = [[] for _ in range(N*3+3)]
for _ in range(M):
    u,v = map(int,input().split())
    path[u].append(v)

S,T = map(int,input().split())
import collections

q = collections.deque()
vis = [[-1 for _ in range(3)] for _ in range(N+3)]
def bfs():
    while len(q) > 0:
        now,cnt = q.popleft()
        step = cnt % 3
        if now == T and step  == 0:  
            return cnt
        for x in path[now]:
            if vis[x][(step+1)%3] == -1:
                vis[x][(step+1)%3] = cnt
                q.append((x,cnt+1))
    return -3
vis[S][0] = 1
q.append([S,0])
print(bfs()//3)




