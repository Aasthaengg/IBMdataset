import sys

INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())

sys.setrecursionlimit(10 ** 9)


def main():
    T, X = MAP()
    print(T/X)


if __name__ == '__main__':
    main()
