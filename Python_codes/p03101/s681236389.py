import sys

INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())

sys.setrecursionlimit(10 ** 9)


def main():
    H, W = MAP()
    h, w = MAP()
    print((H - h)*(W - w))


if __name__ == '__main__':
    main()