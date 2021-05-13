from collections import deque
n = int(input())
v = {i:[] for i in range(n)}
for i in range(n):
    u = list(map(int, input().split()))
    for j in range(2, 2+u[1]):
        v[u[0]-1].append(u[j]-1)

global cnt1 
cnt1 = 0
visited = [False for _ in range(n)]
f = [0 for _ in range(n)]
l = [0 for _ in range(n)]
def DFS(now, visited):
    global cnt1
    cnt1 += 1
    f[now] = cnt1
    visited[now] = True
    for nv in v[now]:
        if visited[nv]:
            continue
        DFS(nv, visited)
    cnt1 += 1
    l[now] = cnt1

for value in range(n):
    if not visited[value]:
        DFS(value, visited)
    
for i in range(n):
    print(i+1, f[i], l[i])
