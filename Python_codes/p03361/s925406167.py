import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    S = [readline().strip() for _ in range(H)]

    def check(i, j):
        if (
            i - 1 >= 0
            and S[i - 1][j] == '#'
            or i + 1 < H
            and S[i + 1][j] == '#'
            or j - 1 >= 0
            and S[i][j - 1] == '#'
            or j + 1 < W
            and S[i][j + 1] == '#'
        ):
            return True
        else:
            return False

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                ok = check(i, j)
                if not ok:
                    print('No')
                    return

    print('Yes')
    return


if __name__ == '__main__':
    main()
