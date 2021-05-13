import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, readline().split())

    for x in range(1, 1500):
        if 8 * x // 100 == A and 10 * x // 100 == B:
            print(x)
            return

    print('-1')
    return


if __name__ == '__main__':
    main()
