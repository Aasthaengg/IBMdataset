import queue
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
ab = []
for _ in range(N - 1):
    ab.append(tuple(map(int, input().split())))

G = [[] for _ in range(N + 1)]
for el in ab:
    a, b = el
    G[a].append(b)
    G[b].append(a)

seen = [False] * (N + 1)
todo = queue.Queue()
dist = [0] * (N + 1)
prev = [None] * (N + 1)

def bfs(parent):
    seen[parent] = True
    for child in G[parent]:
        if seen[child] == False:
            todo.put(child)
            dist[child] = dist[parent] + 1
            prev[child] = parent
    if not todo.empty():
        bfs(todo.get())

bfs(1)
#print(dist)
#print(prev)
min_dist = dist[N]
#print(min_dist)

route = []
temp = N
for _ in range(min_dist + 1):
    route.append(temp)
    temp = prev[temp]
#print(route)


seen = [False] * (N + 1)
def dfs(parent):
    seen[parent] = True
    cnt[0] += 1
    for child in G[parent]:
        if seen[child] == False:
            dfs(child)


S = route[(min_dist + 1) // 2 - 1]
F = route[(min_dist + 1) // 2]

seen[S] = True
seen[F] = True
cnt = [0]
dfs(S)
arround_S = cnt[0]
cnt = [0]
dfs(F)
arround_F = cnt[0]
#print(arround_N, arround_1)

if arround_F > arround_S:
    print('Fennec')
else:
    print('Snuke')




