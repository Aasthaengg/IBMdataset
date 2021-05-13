import sys
from itertools import permutations
def input(): return sys.stdin.readline().strip()


def main():
    N, M, num = map(int, input().split())
    R = list(map(int, input().split()))

    # 全点対間最短距離を予め求めておく（ワーシャルフロイド）
    path = [[10**18] * N for _ in range(N)]
    for i in range(N): path[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        path[a - 1][b - 1] = min(c, path[a - 1][b - 1])
        path[b - 1][a - 1] = min(c, path[b - 1][a - 1])
    for k in range(N):
        for i in range(N):
            for j in range(N):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])

    # あとはRの全順列に対して一つずつ評価すれば良い
    ans = 10**18
    for r in list(permutations(R)):
        d = 0
        for i in range(num - 1):
            d += path[r[i] - 1][r[i + 1] - 1]
        ans = min(ans, d)
    print(ans)


if __name__ == "__main__":
    main()
