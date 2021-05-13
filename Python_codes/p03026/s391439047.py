from heapq import heappush, heappop, heapify
from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    ai, bi = map(lambda x: int(x) - 1, input().split())
    G[ai].append(bi)
    G[bi].append(ai)


# 大きい数字から順番に割り当てる
C = list(map(lambda x: -int(x), input().split()))
heapify(C)
score = -sum(C) + min(C)

# どこかの葉にmaxを置いて，そこから順番に置く
# => maxの値は葉のスコア計算で消えてOK
leaf = -1
for n in range(N):
    if len(G[n]) == 1:
        leaf = n
        break

# 深さ優先で全探索
queue = [leaf]
ans = [-1] * N
while queue:
    node = queue.pop()
    for neighbor in G[node]:
        if ans[neighbor] == -1:
            ans[neighbor] = -heappop(C)
            queue.append(neighbor)

print(score)
print(*ans)