from collections import deque

n = int (input())
roots = [[] for _ in range(2*n)]
color = [0] * 2 * n

for i in range(n-1):
    u, v, w = [int(i) for i in input().split()]
    u = u - 1
    v = v - 1

    if (w % 2 == 1):
        roots[u].append(v)
        roots[v].append(u)
    else:
        roots[u].append(u+n)
        roots[u+n].append(v)
        roots[v].append(v+n)
        roots[v+n].append(u)

d = deque()
d.append(0)
color[0] = 1

while(len(d)):
    temp = d.popleft()
    for i in roots[temp]:
        if(color[i] == 0):
            color[i] = color[temp] * (-1)
            d.append(i)

for i in range(n):
    print(max(0,color[i]))