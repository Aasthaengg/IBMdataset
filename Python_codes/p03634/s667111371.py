n = int(input())
V = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    V[a].append([b,c])
    V[b].append([a,c])
q,k = map(int,input().split())
from collections import deque
dis = [-1]*(n+1)
Q = deque([])
Q.append(k)
dis[k] = 0
while Q:
    r = Q.popleft()
    for A,D in V[r]:
        if dis[A] == -1:
            Q.append(A)
            dis[A] = dis[r] + D
x = [0]*q
for i in range(q):
    x,y = map(int,input().split())
    print(dis[x]+dis[y])