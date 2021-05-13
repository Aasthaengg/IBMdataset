from collections import deque
N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
nord = [0]*N
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
for i in range(Q):
    a, b = map(int, input().split())
    nord[a-1] += b

d = deque()
d.append(0)
Done = [-1]*N

while d:
    x = d.popleft()
    for i in edge[x]:
        if Done[i] != -1:
            continue
        nord[i] += nord[x]
        d.append(i)
    Done[x] += 1

for i in nord:
    print(i)
