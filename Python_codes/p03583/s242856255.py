import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    for h in range(1, 3501):
        for n in range(1, 3501):
            denom = 4 * h * n - N * n - N * h
            numer = N * h * n
            if denom > 0 and numer % denom == 0:
                print(h, n, numer // denom)
                return

    return


if __name__ == '__main__':
    main()
