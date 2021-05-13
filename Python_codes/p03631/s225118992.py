import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = input()
    if N == N[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
