# coding: utf-8
# Your code here!

import itertools

N, M = map(int, input().split())

graph= [[False]*N for i in range(N)]

for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a][b] = True
    graph[b][a] = True

lst = [i-1 for i in range(N)]
cnt = 0

for v in itertools.permutations(lst, N):
    if v[0] != 0:
        continue
    for i in range(N-1):
        if graph[v[i]][v[i+1]] == False:
            break
        if i == N-2:
            cnt += 1

print(cnt)







