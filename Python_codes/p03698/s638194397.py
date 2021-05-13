import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    if len(S) == len(set(S)):
        print('yes')
    else:
        print('no')

    return


if __name__ == '__main__':
    main()
