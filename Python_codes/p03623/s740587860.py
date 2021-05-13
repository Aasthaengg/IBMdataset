import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    x, a, b = map(int, readline().split())

    if abs(x - a) < abs(x - b):
        print('A')
    else:
        print('B')

    return


if __name__ == '__main__':
    main()
