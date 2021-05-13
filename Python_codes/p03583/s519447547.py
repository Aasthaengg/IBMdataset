import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())

    for h in range(1, 3501):
        for n in range(1, 3501):
            if 4 * h * n - N * n - N * h > 0:
                w = (N * h * n) / (4 * h * n - N * n - N * h)
                if w.is_integer() and w > 0 and 4 * h * n * w == N * n * w + N * h * w + N * h * n:
                    print(h, n, int(w))
                    exit()


if __name__ == '__main__':
    resolve()
