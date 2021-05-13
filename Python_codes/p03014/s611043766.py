import sys
from itertools import groupby

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def len_count(S):
    H, W = len(S), len(S[0])
    L = [[0] * W for _ in range(H)]
    for row_S, row_L in zip(S, L):
        vec = [1]
        for i in range(1, W):
            if row_S[i - 1] == row_S[i]:
                vec[-1] += 1
            else:
                vec.append(1)

        idx = 0
        valid = row_S[0] == '.'
        for n in vec:
            if valid:
                for i in range(idx, idx + n):
                    row_L[i] = n
            idx += n
            valid = not valid

    return L


def main():
    H, W = map(int, readline().split())
    S = [readline().strip() for _ in range(H)]

    L1 = [[0] * W for _ in range(H)]
    for x in range(H):
        vec = [1]
        for i in range(1, W):
            if S[x][i - 1] == S[x][i]:
                vec[-1] += 1
            else:
                vec.append(1)

        idx = 0
        valid = S[x][0] == '.'
        for n in vec:
            if valid:
                for i in range(idx, idx + n):
                    L1[x][i] = n
            idx += n
            valid = not valid

    L2 = [[0] * W for _ in range(H)]
    for y in range(W):
        vec = [1]
        for i in range(1, H):
            if S[i - 1][y] == S[i][y]:
                vec[-1] += 1
            else:
                vec.append(1)

        idx = 0
        valid = S[0][y] == '.'
        for n in vec:
            if valid:
                for i in range(idx, idx + n):
                    L2[i][y] = n
            idx += n
            valid = not valid

    ans = 0
    for i in range(H):
        for j in range(W):
            if ans < L1[i][j] + L2[i][j] - 1:
                ans = L1[i][j] + L2[i][j] - 1

    print(ans)
    return


if __name__ == '__main__':
    main()
