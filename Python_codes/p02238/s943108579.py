from collections import deque
n = int(input())
data = [None]*n
unvisited = [1]*n
for _ in range(n):
    a,*b = map(int,input().split())
    a -= 1
    data[a] = deque([i-1 for i in b[1:]])

d = [-1]*n
f = [-1]*n
t = 0

dq = deque([])
for u in range(n):
    if unvisited[u]:
        dq.append(u)
        unvisited[u] = 0
        t += 1
        d[u] = t
        while dq:
            k = dq[-1]
            if data[k]:
                v = data[k].popleft()
                if unvisited[v]:
                    unvisited[v] = 0
                    t += 1
                    d[v] = t
                    dq.append(v)
            else:
                dq.pop()
                t += 1
                f[k] = t

for i in range(n):
    print(i+1,d[i],f[i])
