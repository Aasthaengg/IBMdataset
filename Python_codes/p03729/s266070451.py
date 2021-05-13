import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C = readline().split()

    if A[-1] == B[0] and B[-1] == C[0]:
        print('YES')
    else:
        print('NO')

    return


if __name__ == '__main__':
    main()
