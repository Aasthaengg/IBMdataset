import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, C = map(int, input().split())
    D = [[0] * (C + 1)]
    for _ in range(C):
        d = [0] + list(map(int, input().split()))
        D.append(d)

    grid = [[0] * (N + 1)]
    for _ in range(N):
        g = [0] + list(map(int, input().split()))
        grid.append(g)

    cost = {0: [], 1: [], 2: []}
    ans = INF
    for c in range(1, C + 1):
        cost0 = 0
        cost1 = 0
        cost2 = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if (i + j) % 3 == 0:
                    cost0 += D[grid[i][j]][c]
                elif (i + j) % 3 == 1:
                    cost1 += D[grid[i][j]][c]
                elif (i + j) % 3 == 2:
                    cost2 += D[grid[i][j]][c]

        cost[0].append((c, cost0))
        cost[1].append((c, cost1))
        cost[2].append((c, cost2))

    cost[0].sort(key=lambda x: x[1])
    cost[1].sort(key=lambda x: x[1])
    cost[2].sort(key=lambda x: x[1])

    ans = INF
    for c0, cost0 in cost[0][:3]:
        for c1, cost1 in cost[1][:3]:
            for c2, cost2 in cost[2][:3]:
                if c0 == c1 or c1 == c2 or c2 == c0:
                    continue

                tmp = cost0 + cost1 + cost2
                if tmp < ans:
                    ans = tmp

    print(ans)


if __name__ == "__main__":
    main()
