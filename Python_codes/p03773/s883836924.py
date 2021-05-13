import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    print((A+B)%24)


if __name__ == '__main__':
    main()