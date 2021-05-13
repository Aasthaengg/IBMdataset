from collections import deque
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

dist_f = [None]*n
dist_s = [None]*n

que = deque([(0,0)])
while que:
    node, cost = que.popleft()
    if dist_f[node] != None:
        continue
    dist_f[node] = cost
    for to in g[node]:
        que.append((to, cost+1))

que = deque([(n-1, 0)])
while que:
    node, cost = que.popleft()
    if dist_s[node] != None:
        continue
    dist_s[node] = cost
    for to in g[node]:
        que.append((to, cost+1))
        
cnt = 0
for i in range(n):
    if dist_f[i] <= dist_s[i]:
        cnt += 1
print('Fennec' if cnt>n-cnt else 'Snuke')