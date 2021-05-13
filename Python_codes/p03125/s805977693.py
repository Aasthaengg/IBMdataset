import sys

INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())

sys.setrecursionlimit(10 ** 9)


def main():
    A, B = MAP()
    print(A + B if B % A == 0 else B - A)


if __name__ == '__main__':
    main()