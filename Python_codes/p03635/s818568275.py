import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = map(int, readline().split())
    print((N-1)*(M-1))

if __name__ == '__main__':
    main()
