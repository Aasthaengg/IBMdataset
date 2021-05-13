import sys
from heapq import heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *A = map(int, read().split())

    hq = []
    for a in A:
        heappush(hq, -a)

    for _ in range(M):
        a = heappop(hq)
        a = int(a / 2)
        heappush(hq, a)

    print(-sum(hq))
    return


if __name__ == '__main__':
    main()
