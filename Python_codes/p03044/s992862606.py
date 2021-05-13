#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right

def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        adj[u-1].append((v-1,w))
        adj[v-1].append((u-1,w))
    
    queue = deque([0])
    visit = [-1] * N
    visit[0] = 1
    
    while queue:
        now = queue.popleft()
        for u,w in adj[now]:
            if visit[u] < 0:
                queue.append(u)
                if w % 2 == 0:
                    visit[u] = visit[now]
                else:
                    visit[u] = (visit[now]+1) % 2
    [print(v) for v in visit]


if __name__ == "__main__":
    main()
