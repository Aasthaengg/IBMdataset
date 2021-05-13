from _collections import defaultdict
import sys
import collections
import sys
sys.setrecursionlimit(10**6)


def get_ls():
    return list(map(int, input().split()))


def longest_path_util(node, graph, dp):

    res = 0

    if dp[node] != -1:
        return dp[node]

    for neib in graph[node]:
        res = max(res, longest_path_util(neib, graph, dp) + 1)

    dp[node] = res

    return dp[node]


graph = defaultdict(list)

[n, k] = get_ls()

dp = [-1] * n

for _ in range(k):
    [x, y] = get_ls()
    graph[x - 1].append(y - 1)

ans = 0

for i in range(n):
    ans = max(ans, longest_path_util(i, graph, dp))

print(ans)




