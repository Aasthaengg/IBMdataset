from collections import deque

def dfs(x):
    INF = 10**9
    q = deque()
    q.append(x)
    d = [INF] * n
    d[x] = 0
    while q:
        f = q.pop()
        now = d[f]
        for ce in e[f]:
            if d[ce] == INF:
                d[ce] = now + 1
                q.append(ce)
    return d    


n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

    
d0 = dfs(0)
dn = dfs(n-1)
f = 0
for i in range(n):
    if d0[i] <= dn[i]:
        f += 1
s = n - f
print('Fennec') if f > s else print('Snuke')