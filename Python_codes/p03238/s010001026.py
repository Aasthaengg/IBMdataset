import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    if N == 1:
        print('Hello World')
    else:
        A, B = map(int, read().split())
        print(A + B)

    return


if __name__ == '__main__':
    main()
