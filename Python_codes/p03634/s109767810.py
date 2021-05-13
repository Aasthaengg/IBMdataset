"""
--- アルゴリズム概要 ---
前計算で頂点Kから各ノードへの最短路を記録しておき、
各クエリに対しては、dp[a]+dp[b]を返せばよい。

頂点Kから各ノードへの最短ルートはdfsとかで記録していけばよい。
"""
def main():
    from collections import deque
    import sys
    sys.setrecursionlimit(20000000)
    input = sys.stdin.readline
    N = int(input())
    AB = [[]for _ in range(N+1)]
    for i in range(N-1):
        a,b,c = map(int,input().split())
        AB[a].append((b,c))
        AB[b].append((a,c))

    Q,K = map(int,input().split())

    path = {K:""}
    dp = [0]*(N+1)
    que = deque()
    for n,c in AB[K]:
        que.append((n,c))
    while que:
        now,cost = que.pop()
        path[now]=""
        dp[now]=cost
        for n,c in AB[now]:
            if n not in path:
                que.append((n,cost+c))
    for i in range(Q):
        x,y=map(int,input().split())
        print(dp[x]+dp[y])
main()