import sys

INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())

sys.setrecursionlimit(10 ** 9)


def main():
    R = INT()

    if R < 1200: print("ABC")
    elif R < 2800: print("ARC")
    else: print("AGC")


if __name__ == '__main__':
    main()