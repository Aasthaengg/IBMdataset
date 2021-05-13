import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N = int(readline())
    for h in range(1, 3501):
        for n in range(1, 3501):
            if (4 * h * n - N * n - N * h) != 0:
                w = (N * h * n) / (4 * h * n - N * n - N * h)
                if w == int(w) and w != 0 and (h * n * w) != 0 and w > 0:
                    if 4 / N == (n * w + h * w + h * n) / (h * n * w):
                        print(h, n, int(w))
                        exit()


if __name__ == '__main__':
    solve()
