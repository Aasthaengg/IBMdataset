import sys
import heapq


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(a)
    for _ in range(m):
        price = heapq.heappop(a)
        heapq.heappush(a, -((-price) // 2))
    print(-sum(a))


if __name__ == "__main__":
    main()
