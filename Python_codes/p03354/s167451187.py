# D - Equals

from collections import deque

N, M = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]

neighbor = [[] for _ in range(N)]
for idx in range(M):
    neighbor[xy[idx][0]-1].append(xy[idx][1]-1)
    neighbor[xy[idx][1]-1].append(xy[idx][0]-1)
    
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