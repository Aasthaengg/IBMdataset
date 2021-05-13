#BFS
from collections import deque
from sys import stdin
input = stdin.readline

N,M = map(int, input().split())
neighbor = [[] for _ in range(N)]
for i in range(M):
    a,b = map(lambda x: int(x) - 1, input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)

checked = [0]*N
queue = deque()
group = [0]*N
groupnum = 0
for i in range(N):
    if group[i] == 0:
        groupnum += 1
        queue.append(i)
        group[i] = groupnum
        while queue:
            x = queue.popleft()
            for p in neighbor[x]:
                if group[p] == 0:
                    queue.append(p)
                    group[p] = groupnum

group_membercnt = [0]*(N+1)
for num in group:
    group_membercnt[num] += 1
print(max(group_membercnt[1:]))