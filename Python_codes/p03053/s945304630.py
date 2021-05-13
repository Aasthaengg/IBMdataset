
import sys
sys.setrecursionlimit(1000000)
from collections import deque

H, W = map(int, input().split())
#配列の入力
data = [list(input()) for _ in range(H)]

memo = [[-1 for _ in range(W)]for _ in range(H)]
que = deque()

for h in range(H):
    for w in range(W):
        if data[h][w] == '#':
            memo[h][w] = 0
            que.append((h, w))

offset = ((-1, 0), (1, 0), (0, -1), (0, 1))
while que:
    now_h, now_w = que.popleft()
    for nh, nw in offset:
        if now_h+nh < 0 or H-1 < now_h+nh or now_w+nw < 0 or W-1 < now_w+nw:
            continue

        if memo[now_h+nh][now_w+nw] >= 0:
            continue

        memo[now_h+nh][now_w+nw] = memo[now_h][now_w]+1
        que.append((now_h+nh,now_w+nw))


ans = -1
for h in range(H):
    ans = max(ans, max(memo[h]))
print(ans)
