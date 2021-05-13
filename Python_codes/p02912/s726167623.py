import heapq
def main():
    n, m = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t = list(map(lambda x: x*(-1), t))
    heapq.heapify(t)
    while m > 0:
        v = heapq.heappop(t) * -1
        heapq.heappush(t, (v // 2)* -1)
        m -= 1

    print(sum(t)*-1)


if __name__ == '__main__':
    main()