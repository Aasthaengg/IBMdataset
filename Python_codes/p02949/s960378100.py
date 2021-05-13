from collections import deque
N,M,P = map(int,input().split())
INF = 10**18
edge = []
rev_edge = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
dis[1] = 0
for i in range(M):
    A,B,C = map(int,input().split())
    edge.append((A,B,P-C))
    rev_edge[B].append(A)
d = deque()
can_arrive = set()
d.append(N)
can_arrive.add(N)
while d:
    x = d.popleft()
    for y in rev_edge[x]:
        if not y in can_arrive:
            d.append(y)
            can_arrive.add(y)

for i in range(N):
    update = False
    for j in range(M):
        A,B,cost = edge[j]
        if dis[A] != INF and dis[B] > dis[A]+cost:
            dis[B] = dis[A]+cost
            if B in can_arrive:
                update = True
ans = dis[N]
if update:
    print(-1)
else:
    print(max(0,-ans))