import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

G = []
dp = []

def rec(v):
    global dp
    if dp[v] != -1:
        return dp[v]
    ans = 0
    for node in G[v]:
        ans = max(ans, rec(node) + 1)
    dp[v] = ans
    return dp[v]

def main():
    global G, dp
    n, m = list(map(int, input().strip().split()))
    G = [[] for _ in range(n)]
    dp = [-1] * n
    for i in range(m):
        p, q = list(map(int, input().strip().split()))
        p -= 1
        q -= 1
        G[p].append(q)
    ans = 0
    for i in range(n):
        r = rec(i)
        # print("r: ", r)
        ans = max(ans, r)
    print(ans)


if __name__ == '__main__':
    main()
