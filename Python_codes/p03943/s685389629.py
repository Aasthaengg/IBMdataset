import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    C = list(map(int, readline().split()))
    C.sort()

    if C[0] + C[1] == C[2]:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
