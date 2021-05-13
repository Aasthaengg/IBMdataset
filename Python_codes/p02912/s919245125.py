import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Am = [0] * N
    for i in range(N):
        Am[i] = -A[i]

    heapq.heapify(Am)

    for _ in range(M):
        a = heapq.heappop(Am)
        a = -a
        a = a // 2
        a = -a
        heapq.heappush(Am, a)

    print(-sum(Am))


if __name__ == '__main__':
    solve()
