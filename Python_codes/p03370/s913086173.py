import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, X = map(int, readline().split())
    M = list(int(readline()) for _ in range(N))
    ans = N + (X-sum(M))//min(M)
    print(ans)


if __name__ == '__main__':
    main()
