import heapq


def main():
    n = int(input())
    As = sorted(list(map(int, input().split())))[::-1]
    ans = 0
    q = []
    heapq.heappush(q, -As[0])
    for i in range(1, n):
        tmp = -heapq.heappop(q)
        ans += tmp
        heapq.heappush(q, -As[i])
        heapq.heappush(q, -As[i])
    print(ans)


if __name__ == "__main__":
    main()
