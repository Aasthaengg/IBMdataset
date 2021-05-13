def main():
    from itertools import product
    import heapq

    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]

    l = [[0, 0], [1, 0], [0, 1], [1, 1]]
    r = range(4)
    ans = []
    heapq.heapify(ans)
    for c in product(r, r, r, r, r):
        v = [l[i] for i in c]
        s = sum(v, [])
        if sum(s) == 0:
            continue
        t = sum(y[sum([i * j for i, j in zip(s, x)])] for x, y in zip(f, p))
        heapq.heappush(ans, -t)

    print(-1 * heapq.heappop(ans))


if __name__ == '__main__':
    main()
