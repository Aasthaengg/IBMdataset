from collections import deque

N = int(input())

edge = [[int(s) - 1 for s in input().split()] for _ in range(N-1)]
graph = [[] for _ in range(N)]
weight_odd = {}

for i, j, w in edge:
    graph[i].append(j)
    graph[j].append(i)
    weight_odd[(i, j)] = (w % 2 != 0)
    weight_odd[(j, i)] = (w % 2 != 0)

dq = deque([0])
visited = [False] * N
color = [1] * N
while(dq):
    search_obj = dq.pop()
    col1 = color[search_obj]
    col2 = 0 if col1 == 1 else 1
    for candidate_obj in graph[search_obj]:
        if not visited[candidate_obj]:
            if weight_odd[(candidate_obj, search_obj)]:
                color[candidate_obj] = col1
            else:
                color[candidate_obj] = col2
            dq.appendleft(candidate_obj)
            visited[candidate_obj] = True

for c in color:
    print(c)