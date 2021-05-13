import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, A, B = map(int, readline().split())
    print(min(A,B), max((A+B)-N, 0))


if __name__ == '__main__':
    main()
