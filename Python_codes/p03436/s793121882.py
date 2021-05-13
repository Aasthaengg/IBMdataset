import collections

h, w = map(int, input().split())
s = []
count = 0
s.append("#" * (w + 2))
for i in range(h):
    temp = input()
    count += temp.count(".")
    s.append("#" + temp + "#")
s.append("#" * (w + 2))
dis = [[float("inf") for i in range(w + 2)] for i in range(h + 2)]
dis[1][1] = 0
p = collections.deque([[1, 1]])
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while p:
    temp = p.popleft()
    x, y = temp[0], temp[1]
    for i in d:
        dx, dy = i[0], i[1]
        if s[y + dy][x + dx] == "#":
            continue
        else:
            if dis[y][x] + 1 < dis[y + dy][x + dx]:
                dis[y + dy][x + dx] = dis[y][x] + 1
                p.append([x + dx, y + dy])
if dis[h][w] == float("inf"):
    print(-1)
else:
    print(count - dis[h][w] - 1)