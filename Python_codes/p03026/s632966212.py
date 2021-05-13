from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
G = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    degree[a] += 1
    degree[b] += 1
c = list(map(int, input().split()))
c.sort(reverse=True)

heap = []
for i in range(1, N+1):
    heappush(heap, (degree[i], i))

M = 0
num = [0] * (N+1)
while heap:
    d, i = heappop(heap)
    if num[i] != 0:
        continue
    num[i] = c.pop()
    for j in G[i]:
        if num[j] == 0:
            M += num[i]
            degree[i] -= 1
            degree[j] -= 1
            heappush(heap, (degree[j], j))
print(M)
print(' '.join(map(str, num[1:])))