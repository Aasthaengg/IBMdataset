from collections import deque
n,m = map(int,input().split())
path = [set() for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    path[u].add(v)

s,t = map(int,input().split())

que = deque([(s-1,0)])
d = [[float('inf')]*n for _ in range(3)]
d[0][s-1] = 0
while que:
    p,i = que.popleft()
    j = (i+1)%3
    for to in path[p]:
        if d[j][to] == float('inf'):
            d[j][to] = d[i][p] + 1
            que.append((to,j))
if d[0][t-1] == float('inf'):
    d[0][t-1] = -3
print(d[0][t-1]//3)
