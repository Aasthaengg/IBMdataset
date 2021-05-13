import sys
from heapq import heappush, heappop
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    ab = []

    for i in range(N):
        a, b = in_nn()
        ab.append((a + b, a, b))

    ab.sort(reverse=True)

    taka = 0
    for i in range(0, N, 2):
        taka += ab[i][1]
    aoki = 0
    for i in range(1, N, 2):
        aoki += ab[i][2]

    ans = taka - aoki
    # print(ab)
    print(ans)


if __name__ == '__main__':
    main()
