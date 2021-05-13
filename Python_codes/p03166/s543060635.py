import sys
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def rec(i, dp, nodes):
    # 更新済みのデータの場合はそのまま返す
    if dp[i] != -1:
        return dp[i]

    res = 0
    for next in nodes[i]:
        res = max(res, rec(next, dp, nodes) + 1)
    dp[i] = res
    return res

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    N, M = map(int, input().rstrip().split())
    nodes = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().rstrip().split())
        nodes[x-1].append(y-1)

    # dp[i] = i番目のノードを始点としたときの最大パス長
    dp = [-1] * N
    ans = 0
    for i in range(N):
        ans = max(ans, rec(i, dp, nodes))
    print(ans)


if __name__ == '__main__':
    main()