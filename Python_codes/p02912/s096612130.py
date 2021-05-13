from heapq import heappush, heappop

def resolve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    heap = []
    for i in a:
        heappush(heap, [-i, i, 0])

    for i in range(m):
        num, x, cnt = heappop(heap)
        heappush(heap, [num / 2, x, cnt + 1])

    ans = 0
    for i in range(n):
        num, x, cnt = heappop(heap)
        ans += int(num)
    print(-ans)


if __name__ == "__main__":
    resolve()
