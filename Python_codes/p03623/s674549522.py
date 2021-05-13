import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    x, a, b = map(int, readline().split())
    if abs(x-a)<=abs(x-b):
        print('A')
    else:
        print('B')


if __name__ == '__main__':
    main()
