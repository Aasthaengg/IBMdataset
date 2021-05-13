import sys

INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())

sys.setrecursionlimit(10 ** 9)


def main():
    N = INT()

    if N == 1: print("Hello World")
    else:
        A = INT()
        B = INT()
        print(A + B)


if __name__ == '__main__':
    main()