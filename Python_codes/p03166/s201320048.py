# https://atcoder.jp/contests/dp/tasks/dp_g
import sys
sys.setrecursionlimit(10**7)


class DAG:
    def __init__(self, n):
        # n: num of vertices
        self.n = n
        self.adj = [[] for _ in range(n)]

    def addEdge(self, parent, child):
        self.adj[parent].append(child)

    def dfs(self, node):
        ans = 0
        for child in self.adj[node]:
            ans = max(ans, 1 + self.dfs(child))
        return ans

    def dfsWithMemo(self, node, memo, visited):
        if(visited[node]):
            return memo[node]
        visited[node] = True
        for child in self.adj[node]:
            memo[node] = max(
                memo[node], 1 + self.dfsWithMemo(child, memo, visited))
        return memo[node]

    def dfsWithDp(self, node, dp, visited):
        if(visited[node]):
            return dp[node]
        visited[node] = True
        for child in self.adj[node]:
            if not visited[child]:
                self.dfsWithDp(child, dp, visited)
            dp[node] = max(dp[node], 1 + self.dfsWithDp(child, dp, visited))
        return dp[node]

    # o(n^2) solution
    def findLongestPathNaive(self):
        ans = 0
        for i in range(self.n):
            ans = max(ans, self.dfs(i))
        return ans

    # o(n) solution
    def findLongestPathWithMemo(self):
        visited = [False] * self.n
        memo = [0] * self.n
        ans = 0
        for i in range(self.n):
            ans = max(ans, self.dfsWithMemo(i, memo, visited))
        return ans

    # O(n) solution
    def findLongestPathWithDp(self):
        visited = [False] * self.n
        dp = [0] * self.n  # dp[i] := longest path starting from vertex i
        ans = 0
        for i in range(self.n):
            ans = max(ans, self.dfsWithDp(i, dp, visited))
        return ans


def main():
    N, M = map(int, input().split())
    dag = DAG(N)
    for _ in range(M):
        parent, child = map(lambda i: int(i) - 1, input().split())
        dag.addEdge(parent, child)
    # print(dag.findLongestPathNaive())
    #  print(dag.findLongestPathWithMemo())
    print(dag.findLongestPathWithDp())


main()
