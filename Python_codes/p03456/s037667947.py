import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    n = int(S.replace(' ', ''))

    for i in range(1, 10000):
        if i * i == n:
            print('Yes')
            return

    print('No')
    return


if __name__ == '__main__':
    main()
