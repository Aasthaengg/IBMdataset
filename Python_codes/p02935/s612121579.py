import heapq


def main():
    n = int(input())
    v = list(map(float, input().split()))
    heapq.heapify(v)
    while True:
        a = heapq.heappop(v)
        if not len(v):
            print(a)
            return
        b = heapq.heappop(v)
        heapq.heappush(v, (a + b) / 2)


if __name__ == '__main__':
    main()
