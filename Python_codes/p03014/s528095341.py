import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    H, W = map(int, readline().split())
    S = [readline().strip() for _ in range(H)]

    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]

    for i in range(H):
        c = 0
        for j in range(W):
            if S[i][j] == '#':
                c = 0
            else:
                L[i][j] = c
                c += 1
        c = 0
        for j in range(W - 1, -1, -1):
            if S[i][j] == '#':
                c = 0
            else:
                R[i][j] = c
                c += 1

    for j in range(W):
        c = 0
        for i in range(H):
            if S[i][j] == '#':
                c = 0
            else:
                U[i][j] = c
                c += 1
        c = 0
        for i in range(H - 1, -1, -1):
            if S[i][j] == '#':
                c = 0
            else:
                D[i][j] = c
                c += 1

    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] + 1)

    print(ans)
    return


if __name__ == '__main__':
    main()
