import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b, c = map(int, readline().split())
    if a + b + c - max(a, b, c) == max(a, b, c):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
