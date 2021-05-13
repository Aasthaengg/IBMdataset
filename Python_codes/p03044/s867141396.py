N = int(input())
graph = [[] for  _ in range(N)]
now = 0
for _ in range(N-1):
    x,y,w = map(int,input().split())
    x -= 1
    y -= 1
    graph[x].append((y,w))
    graph[y].append((x,w))
    now = x
    
vis = [0 for _ in range(N)]

even = set()
odd = set()
import sys
sys.setrecursionlimit(10000000)


def dfs(now):
    #print(now)
    for nv in graph[now]:
        if vis[nv[0]]: continue
        if nv[1] % 2 == 0:
            if now in even:
                even.add(nv[0])
            else:
                odd.add(nv[0])
        else:
            if now in even:
                odd.add(nv[0])
            else:
                even.add(nv[0])
        vis[nv[0]] = 1
        dfs(nv[0])
vis[x] = 1
even.add(x)
dfs(x)

for i in range(N):
    if i in even:
        print(1)
    else:
        print(0)

