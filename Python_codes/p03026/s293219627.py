#!/usr/bin python3
# -*- coding: utf-8 -*-

# 双方向グラフで幅優先探索

from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
#隣接リストの作成
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
mx = 0
st = -1
for i, g in enumerate(graph):
    if len(g)>mx:
        st = i
        mx = len(g)
#    print(graph)
c = list(map(int,input().split()))
c.sort(reverse = True)

#幅優先探索
q = deque()
seen = [False]*N
q.append(st)
seen[st] = c[0]
idx = 1
while len(q)>0:
    cur = q.popleft()
    for i in graph[cur]:
        if seen[i]==False:
            seen[i] = c[idx]
            idx += 1
            q.append(i)
print(sum(c[1:]))
print(' '.join(map(str,seen)))