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

    def dfsWithDp(self, node, dp, visited):
        if(visited[node]):
            return dp[node]
        visited[node] = True
        for child in self.adj[node]:
            if not visited[child]:
                self.dfsWithDp(child, dp, visited)
            dp[node] = max(dp[node], 1 + self.dfsWithDp(child, dp, visited))
        return dp[node]

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
    print(dag.findLongestPathWithDp())


main()
