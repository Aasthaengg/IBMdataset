import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    if K==1:
        print(0)
    else:
        print(N-K)

if __name__ == '__main__':
    main()
