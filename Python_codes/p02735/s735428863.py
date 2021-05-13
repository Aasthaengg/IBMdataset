import queue

h, w = map(int, input().split())
s = [input() for i in range(h)]

cost = [[99999999 for j in range(w)] for i in range(h)]

cost[0][0] = 0
xq = queue.Queue()
yq = queue.Queue()
xq.put(0)
yq.put(0)

while xq.qsize() > 0:
    x = xq.get()
    y = yq.get()

    if y + 1 < h:
        tmp = cost[y][x] + (1 if s[y][x] == '.' and s[y + 1][x] == '#' else 0)
        if tmp < cost[y + 1][x]:
            cost[y + 1][x] = tmp
            xq.put(x)
            yq.put(y + 1)
    if x + 1 < w:
        tmp = cost[y][x] + (1 if s[y][x] == '.' and s[y][x + 1] == '#' else 0)
        if tmp < cost[y][x + 1]:
            cost[y][x + 1] = tmp
            xq.put(x + 1)
            yq.put(y)

print((0 if s[0][0] == '.' else 1) + cost[h - 1][w - 1])
