import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, X = map(int, readline().split())
    if A<=X<=A+B:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
