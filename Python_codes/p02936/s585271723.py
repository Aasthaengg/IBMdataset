#%%
#%%
import sys
sys.setrecursionlimit(10 ** 9)

N, Q = [int(i) for i in input().split()]
path = [[] for _ in range(N - 1)]
query = [[] for _ in range(Q)]
for i in range(N - 1):
    path[i] = [int(i) - 1 for i in input().split()]
for i in range(Q):
    query[i] = [int(i) for i in input().split()]
    query[i][0] -= 1
#%%
add = [0] * N
ans = [0] * N
for i, j in query:
    add[i] += j
    
children = [[]  for _ in range(N)]
for i, j in path:
    children[i].append(j)
    children[j].append(i)
    
def DFS(id, parent, value):
    value += add[id]
    ans[id] = value
    for i in children[id]:
        if i == parent:
            continue
        DFS(i, id, value)
    
DFS(0, -1, 0)

for i in ans:
    print(i, end=" ")
