import sys
sys.setrecursionlimit(10**6)
edges, vertices = map(int, input().split())
dp = [None for _ in range(edges)]

nodes = [[] for _ in range(edges)]

for i in range(vertices):
    start, end = map(int, input().split())
    nodes[end -1].append(start-1)

for i in range(edges):
    if not len(nodes[i]):
        dp[i] = 0
def find(arr):
    if not len(arr):
        return 0
    for x in arr:
        if dp[x] is None:
            dp[x] = find(nodes[x])
    return 1 + max(dp[x] for x in arr)

for i in range(edges):
    dp[i] = find(nodes[i])

print(max(dp))
