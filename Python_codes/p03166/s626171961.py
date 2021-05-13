import sys
sys.setrecursionlimit(1000000)
def main():
    n, m = [int(x) for x in input().split()]
    global dp
    dp = [-1]*n
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        x -= 1
        y -= 1

        grafo[x].append(y)

    resp = 0
    for u in range(n):
        resp = max(dfs(u, grafo), resp)

    print(resp)
        

def dfs(u, grafo):
    global dp

    if len(grafo[u]) == 0:
        dp[u] = 0
        return dp[u]

    if dp[u] != -1:
        return dp[u]


    for v in grafo[u]:
        dp[u] = max(dfs(v, grafo) + 1, dp[u])

    return dp[u]
        
main()