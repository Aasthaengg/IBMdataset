import sys

INPUT = lambda: sys.stdin.readline().rstrip()
MAP = lambda: map(int, INPUT().split())

sys.setrecursionlimit(10 ** 9)


def main():
    A, B, C = MAP()

    tmp = B
    for i in range(C):
        tmp -= A
        if tmp < 0:
            print(i)
            break
    else:
        print(C)


if __name__ == '__main__':
    main()