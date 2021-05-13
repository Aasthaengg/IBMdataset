from collections import deque
n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append((b,c))
    e[b].append((a,c))

Q,k = map(int,input().split())
k -= 1
d = [-1]*n
d[k] = 0
q =deque([])
q.append(k)
while q:
    now = q.popleft()

    for nex,dis in e[now]:
        if d[nex] == -1:
            d[nex] = d[now]+dis
            q.append(nex)

for i in range(Q):
    x,y = map(int,input().split())
    print(d[x-1]+d[y-1])

