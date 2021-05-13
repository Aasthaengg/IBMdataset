n = int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
f = 0
s = 0
from collections import deque
ps = [-1] * n
used = [False] * n
used[0] = True # 始めどこから行くか
q = deque([0])
while len(q) > 0:
    a = q.popleft()
    if a == n-1:
        break
    for u in edges[a]:
        if not used[u]:
            ps[u] = a
            q.append(u)
            used[u] = True

nx = n - 1
xs = [n-1]
while nx != 0:
    nx = ps[nx]
    xs.append(nx)

xs.reverse()
l = len(xs) - 2
f = (l+1)//2
s = l-f

if len(xs) == 2:
    z_lim = -1
    n_lim = 0
else:
    z_lim = (len(xs)+1)//2
    n_lim = z_lim - 1

# bfs 0側
used = [-1] * n
used[0] = 0 
q = deque([0])
cnt = 0
while len(q) > 0:
    a = q.popleft()
    for u in edges[a]:
        if used[u] == -1 and u != xs[z_lim]:
            q.append(u)
            used[u] = 0
            cnt += 1
# print("cnt",cnt)
f += cnt

# bfs n-1側
used = [-1] * n
used[n-1] = 0 
q = deque([n-1])
cnt = 0
while len(q) > 0:
    a = q.popleft()
    for u in edges[a]:
        if used[u] == -1 and u != xs[n_lim]:
            q.append(u)
            used[u] = 0
            cnt += 1

s += cnt
# print("z_lim",z_lim,"nlim",n_lim)
# print("f",f,"s",s)
if f > s:
    print("Fennec")
else:
    print("Snuke")
