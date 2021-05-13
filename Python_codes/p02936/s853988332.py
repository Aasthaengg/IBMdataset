import sys
import numpy as np
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    clist = [0]*(n+1)

    for _ in range(q):
        p, x = map(int, input().split())
        clist[p] += x

    dist = [-1] * (n+1)
    dist[0] = 0
    dist[1] = 0

    ans = [0]*(n+1)
    d = deque()
    d.append(1)
    ans[1]=clist[1]
    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            ans[i]=ans[v]+clist[i]
            d.append(i)
    
    ans = ans[1:]
    print(*ans, sep=" ")


if __name__ == '__main__':
    main()