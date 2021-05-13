import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = readline().strip()

    if N[0] == N[1] == N[2] or N[1] == N[2] == N[3]:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
