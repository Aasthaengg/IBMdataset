import sys
import math
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())

    D = []
    for i in range(N):
        a, b = map(int, input().split())
        heapq.heappush(D, (a, b))
    ans = 0
    while M > 0:
        a, b = heapq.heappop(D)
        if M > b:
            ans += a * b
            M -= b
        else:
            ans += M * a
            print(ans)
            exit()


if __name__ == "__main__":
    main()
