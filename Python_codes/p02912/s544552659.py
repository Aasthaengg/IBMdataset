# ABC141D - Powerful Discount Tickets
from heapq import heapify, heappop, heappush


def main():
    _, M = map(int, input().split())
    A = [-i for i in map(int, input().split())]
    heapify(A)

    discount = lambda: heappush(A, -(-heappop(A) // 2))
    for _ in range(M):
        discount()

    print(-sum(A))


if __name__ == "__main__":
    main()
