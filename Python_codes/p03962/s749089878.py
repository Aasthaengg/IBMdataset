import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    P = set(map(int, readline().split()))

    print(len(P))

    return


if __name__ == '__main__':
    main()
