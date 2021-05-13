import heapq
H, W = map(int, input().split())
S = [list(input()) for i in range(H)]
count_black = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            count_black += 1
is_visited = [[False for j in range(W)] for i in range(H)]
q = []
heapq.heappush(q, (1, (0, 0)))
is_visited[0][0] = True
lrud = [[0, -1], [0, 1], [-1, 0], [1, 0]]
while q:
    cost, (x, y) = heapq.heappop(q)
    if x == H-1 and y == W-1:
        break
    for dx, dy in lrud:
        if 0 <= x + dx < H and 0 <= y + dy < W and \
            S[x+dx][y+dy] == '.' and not is_visited[x+dx][y+dy]:
            heapq.heappush(q, (cost+1, (x+dx, y+dy)))
            is_visited[x+dx][y+dy] = True
if x == H-1 and y == W-1:
    print(H*W-count_black-cost)
else:
    print(-1)