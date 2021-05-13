# D - Equals

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
xy = sys.stdin.readlines()

neighbor = [[] for _ in range(N)]
for idx in range(M):
    x,y = map(int, xy[idx].split())
    neighbor[x-1].append(y-1)
    neighbor[y-1].append(x-1)
    
can_swap = []
visited = [-1]*N

for start in range(N):
    if visited[start] == -1:
        tmp = [start] # startから到達可能なpointのリスト
        d = deque([start])
        while d:
            current_point = d.pop()
            visited[current_point] = 1
            for next_point in neighbor[current_point]:
                if visited[next_point] == -1:
                    d.append(next_point)
                    tmp.append(next_point)
        can_swap.append(tmp)                

ans = 0
for idx_group in can_swap:
    tmp_p = [p[idx]-1 for idx in idx_group]
    ans += len(set(tmp_p) & set(idx_group))

print(ans)