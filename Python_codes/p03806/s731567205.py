#!python3

import copy

LI = lambda: list(map(int, input().split()))

# input
N, Ma, Mb = LI()
ABC = [LI() for _ in range(N)]

INF = 10 ** 5


def main():
    w = [[INF] * 401 for _ in range(401)]
    w[0][0] = 0
    for a, b, c in ABC:
        l = copy.deepcopy(w)
        for j in range(a, 401):
            for k in range(b, 401):
                l[j][k] = min(w[j][k], w[j - a][k - b] + c)
        w = l

    ans = INF
    n = 400 // max(Ma, Mb) + 1
    for i in range(1, n):
        ans = min(ans, w[Ma * i][Mb * i])
    ans = -1 if ans == INF else ans
    print(ans)


if __name__ == "__main__":
    main()
