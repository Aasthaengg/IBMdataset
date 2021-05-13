import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
es = [collections.deque() for _ in range(n)]
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    es[l].append((l, r, d))
    es[r].append((r, l, -d))

visited = [False] * n
for i in range(n):
    if not visited[i]:
        visited[i] = True
        if len(es[i]) == 0:
            continue
        distances = [float('inf')] * n
        distances[i] = 0
        q = collections.deque()
        for e in es[i]:
            q.append(e)
        while q:
            j, k, d = q.popleft()
            if visited[k] and distances[k] != distances[j] + d:
                print('No')
                exit()
            distances[k] = distances[j] + d
            visited[k] = True
            while es[k]:
                ee = es[k].popleft()
                if len(es[ee[1]]) > 0:
                    q.append(ee)
print('Yes')