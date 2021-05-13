import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    K = int(readline())
    X = int(readline())
    Y = int(readline())
    if N <= K:
        ans = X * N
    else:
        ans = X * K + Y * (N - K)
    print(ans)


if __name__ == '__main__':
    main()
