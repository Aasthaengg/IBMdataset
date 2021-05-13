import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().split()

    if len(set(S)) == 3:
        print('Three')
    else:
        print('Four')

    return


if __name__ == '__main__':
    main()
