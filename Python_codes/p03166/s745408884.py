from sys import setrecursionlimit, stdin
setrecursionlimit(10**6)
input = stdin.buffer.readline

def main():
    n, m = map(int, input().split())

    edges = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        edges[x-1].append(y-1)

    dp = [-1] * n
    def dfs(node):
        if len(edges[node]) == 0:
            dp[node] = 0
        else:
            max_len = 0
            for new_node in edges[node]:
                if dp[new_node] == -1:
                    dfs(new_node)
                if max_len < dp[new_node]:
                    max_len = dp[new_node]
            dp[node] = max_len + 1

    for node in range(n):
        if dp[node] == -1:
            dfs(node)

    print(max(dp))

main()