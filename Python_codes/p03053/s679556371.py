from collections import deque
h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]
# '#'の地点をスタートとしてqueに全部入れる
# その際にseenもかねたdist配列を-1で初期化して，スタート地点だけ0にする，（-1のところは未踏）
# タプルでqueに入れると少し早くなるらしい
que = deque()
dist = [[-1] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if C[y][x] == '#':
            que.append((y, x))
            dist[y][x] = 0

while len(que) > 0:
    # 現在地点の座標と距離を取得
    now_y, now_x = que.popleft()
    now_d = dist[now_y][now_x]
    for dy, dx in ((1,0), (-1, 0), (0, 1), (0, -1)):
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_y < h and 0 <= next_x < w:
            if dist[next_y][next_x] == -1:
                # もしまだ見ていない地点ならqueに追加し，distを現在の距離+1に更新する
                que.append((next_y, next_x))
                dist[next_y][next_x] = now_d + 1

print(now_d)
