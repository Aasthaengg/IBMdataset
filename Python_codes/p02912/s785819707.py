import heapq

from typing import List


def main():
    n, m = map(int, input().split())
    v = map(int, input().split())
    print(pdt(v, m))


def pdt(v: List[int], m: int) -> int:
    vv = [-a for a in v]
    heapq.heapify(vv)

    for _ in range(m):
        k = -heapq.heappop(vv)
        k = k // 2
        heapq.heappush(vv, -k)

    return -sum(vv)


if __name__ == '__main__':
    main()
