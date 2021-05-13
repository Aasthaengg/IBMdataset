import heapq
n, m = map(int, input().split())

graph = [set() for _ in range(n)]
side = dict()
ans = [0 for _ in range(m + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    t = (a - 1, b - 1, c)
    side[i] = t
    graph[a-1].add(i)
    graph[b-1].add(i)

for j in range(n):
    D = [(0, 0, j, m), ]
    heapq.heapify(D)
    done = [True for _ in range(n)]

    while D:
        d = heapq.heappop(D)
        if done[d[2]]:
            done[d[2]] = False
            ans[d[3]] = 1

            for i in graph[d[2]]:
                a, b, c = side[i]
                if b == d[2]:
                    a, b = b, a
                if done[b]:
                    heapq.heappush(D, (d[0] + c, ans[i], b, i))

print(m - (sum(ans) - 1))
