from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

dis = [10**10] * n
edges = [[] for _ in range(n)]

for _ in range(m):
    l,r,d = map(int,input().split())
    edges[l-1].append((r-1, d))
    edges[r-1].append((l-1, -d))

for i in range(n):
    if dis[i] == 10**10:
        dis[i] = 0
        q = [i]
        while q:
            l = q.pop()
            for r,d in edges[l]:
                if dis[r] == 10**10:
                    dis[r] = dis[l] + d
                    q.append(r)
                else:
                    if dis[r] - dis[l] != d:
                        print('No')
                        exit()

print('Yes')
