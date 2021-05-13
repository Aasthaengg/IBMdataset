#!/usr/bin/env python3

n, m = map(int, input().split())
high = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


ans = 0
for i in range(n):
    tmp = high[i]
    flg = True
    for nxt in graph[i]:
        if high[nxt] >= tmp:
            flg = False
            break
    if flg:
        ans += 1

print(ans)
