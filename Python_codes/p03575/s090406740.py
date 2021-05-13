
import numpy as np
n,m = list(map(int,input().rstrip().split()))
graph = [[] for _ in range(n)]
route_list = []
for _ in range(m):
    a,b = list(map(int,input().rstrip().split()))
    a -=1
    b -=1
    route_list.append([a,b])
    graph[a].append(b)
    graph[b].append(a)

def dfs(mask, p,graph):
    mask[p] = 1
    if mask.all():
        return True
    nexts = graph[p]
    for n in nexts:
        if mask[n] == 1:
            continue
        else:
            if dfs(mask,n,graph):
                return True
    return False

counter = 0
for r in route_list:
    graph[r[0]].remove(r[1])
    graph[r[1]].remove(r[0])
    mask = np.zeros(len(graph),int)
    if dfs(mask,0,graph) == False:
        counter += 1
    graph[r[0]].append(r[1])
    graph[r[1]].append(r[0])
print(counter)
