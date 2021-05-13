import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C = map(int, readline().split())

    for n in range(1, B):
        if n * A % B == C:
            print('YES')
            return

    print('NO')
    return


if __name__ == '__main__':
    main()
