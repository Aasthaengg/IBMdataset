import heapq
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input())
    A = [-int(i) for i in input().strip().split()]
    heapq.heapify(A)
    ans = 0
    for i in range(2 * n):
        a = heapq.heappop(A)
        if i % 2 == 1:
            ans -= a

    print(ans)


if __name__ == "__main__":
    main()
