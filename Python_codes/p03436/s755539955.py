from queue import Queue
H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
white = 0
for g in G:
    white += g.count('.')
been = [[-1] * W for _ in range(H)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
que = Queue()
que.put((0, 0))
been[0][0] = True
while not que.empty():
    h, w = que.get()
    for dx, dy in d:
        nh = h + dx
        nw = w + dy
        if nh < 0 or H <= nh or nw < 0 or W <= nw:
            continue
        if been[nh][nw] != -1:
            continue
        if G[nh][nw] == '#':
            continue
        been[nh][nw] = been[h][w] + 1
        que.put((nh, nw))
if been[H-1][W-1] == -1:
    print(-1)
else:
    print(white - been[H-1][W-1])