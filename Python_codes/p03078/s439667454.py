import heapq
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ans = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
heapq.heapify(ans)
added = {"0 0 0"}
for _ in range(k):
    w = heapq.heappop(ans)
    print(-w[0])
    i, j, m = w[1:]
    dx = [1, 0, 0]
    dy = [0, 1, 0]
    dz = [0, 0, 1]
    for r in range(3):
        ni, nj, nm = i + dx[r], j + dy[r], m + dz[r]
        if not (ni < x and nj < y and nm < z):
            continue
        g = " ".join(map(str, (ni, nj, nm)))
        if g not in added:
            added.add(g)
            heapq.heappush(ans, (-(a[ni] + b[nj] + c[nm]), ni, nj, nm))
