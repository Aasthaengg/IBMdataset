import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C, D = map(int, read().split())

    print(min(A, B) + min(C, D))

    return


if __name__ == '__main__':
    main()