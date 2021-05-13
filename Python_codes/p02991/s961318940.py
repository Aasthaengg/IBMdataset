#!/usr/bin/env python3
import sys
from collections import deque

def solve(N, M, to, start, goal):
    costs = [float('inf')] * (3*N+3)
    costs[start] = 0

    q = deque([start])

    while len(q) != 0:
        u = q.popleft()
        for v in to[u]:
            if costs[u] + 1 < costs[v]:
                costs[v] = costs[u] + 1
                if v == goal: return costs[v] // 3
                q.append(v)
    return -1



def main():
    N, M = map(int, input().split())
    to = [ [] for _ in range(3*N+3) ]
    for _ in range(M):
        u, v = map(int, input().split())
        for i in range(3):
            to[u + (N+1)*i].append(v + (N+1) * ((i+1)%3))
    S, T = map(int, input().split())
    print(solve(N, M, to, S, T))

if __name__ == '__main__':
    main()
