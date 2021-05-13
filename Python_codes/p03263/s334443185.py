import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    A = [list(map(int, readline().split())) for _ in range(H)]

    odd = []

    for i in range(H):
        for j in range(W):
            if i % 2 == 1:
                j = W - j - 1
            if A[i][j] % 2 == 1:
                odd.append((i + 1, j + 1))

    ans = []
    for (x, y), (z, w) in zip(*[iter(odd)] * 2):
        tmp = []
        tmp.append((x, y))
        while (x, y) != (z, w):
            if x % 2 == 1:
                if y == W:
                    x += 1
                else:
                    y += 1
            else:
                if y == 1:
                    x += 1
                else:
                    y -= 1
            tmp.append((x, y))

        for i in range(len(tmp) - 1):
            ans.append((tmp[i][0], tmp[i][1], tmp[i + 1][0], tmp[i + 1][1]))

    print(len(ans))
    for row in ans:
        print(*row)

    return


if __name__ == '__main__':
    main()
