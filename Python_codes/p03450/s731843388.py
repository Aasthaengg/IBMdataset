N,M = map(int,input().split())

edge = [list(map(int,input().split())) for _ in range(M)]

graph = [[] for _ in range(N)]

for e in edge:
    graph[e[0]-1].append((e[1]-1,e[2]))
    graph[e[1]-1].append((e[0]-1,-e[2]))

level = [None for _ in range(N)]

inconsistent = False

for i in range(N):
    if level[i] is None:
        level[i] = 0
        stack = [i]
        while stack:
            node = stack.pop()
            for adj,cost in graph[node]:
                if level[adj] is None:
                    level[adj] = level[node] + cost
                    stack.append(adj)
                else:
                    if level[adj] != level[node] + cost:
                        inconsistent = True
                        break
    if inconsistent:
        break

if inconsistent:
    print('No')
else:
    print('Yes')