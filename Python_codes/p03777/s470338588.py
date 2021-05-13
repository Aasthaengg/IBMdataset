import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b = input().split()
    if a == b:
        print('H')
    else:
        print('D')


if __name__ == '__main__':
    main()
