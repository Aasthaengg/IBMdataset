import heapq
n, k = map(int, input().split())
sushi = []
for _ in range(n):
    t, d = map(int, input().split())
    sushi.append((d, t-1))

sushi.sort(reverse=True)
used = [False] * n
choose = []
rest = []
cost = 0
kind = 0
for i in range(n):
    d, t = sushi[i]
    if i < k:
        cost += d
        if used[t]:
            heapq.heappush(choose, d)
        else:
            used[t] = True
            kind += 1

    else:
        if not used[t]:
            heapq.heappush(rest, -d)
        used[t] = True


cost += kind ** 2
ans = cost

cnt = min(len(choose), len(rest))
for i in range(cnt):
    cost -= heapq.heappop(choose)
    cost += -heapq.heappop(rest)
    cost += 2 * kind + 1
    kind += 1
    ans = max(ans, cost)

print(ans)
