import sys

INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())

sys.setrecursionlimit(10 ** 9)


def main():
    N, i = MAP()
    print(N - i + 1)


if __name__ == '__main__':
    main()