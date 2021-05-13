import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    if A%2 and B%2:
        print('Odd')
    else:
        print('Even')


if __name__ == '__main__':
    main()
