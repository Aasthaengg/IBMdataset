from collections import Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
n = int(input())
edges = [[] for _ in range(n * 1001)]
memo = []
start = set()
for i in range(n):
    A = list(map(int, input().split()))
    for j in range(n-1):
        if i < A[j] - 1:
            A[j] = i * 1000 + A[j] - 1
        else:
            A[j] = (A[j] - 1) * 1000 + i

    for j in range(n-2):
        edges[A[j]].append(A[j+1])
    memo.append(A[0])

memo = Counter(memo).most_common()
for x, t in memo:
    if t > 1:
        start.add(x)

#閉路検出/最長のパス
d = [-1 for _ in range(1001 * n)]
def dfs(v):
    d[v] = -2
    l = 0
    for to in edges[v]:
        if d[to] == -2:
            print(-1)
            exit()
        if d[to] == -1:
            dfs(to)
        l = max(l, d[to] + 1)
    d[v] = l

if len(start) == 0:
    print(-1)
    exit()
for i in start:
    dfs(i)
print(max(d) + 1)