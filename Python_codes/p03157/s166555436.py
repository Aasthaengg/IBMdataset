import sys
input = sys.stdin.readline
from collections import deque

def main():
    h, w = map(int, input().split())
    tizu = [input().strip() for _ in range(h)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    used = [[False for _ in range(w)] for _ in range(h)]
    
    ans = 0
    for i in range(h):
        for j in range(w):
            if used[i][j]:
                continue
            used[i][j] = True
            queue = deque()
            queue.append([i, j])
            queue.append(tizu[i][j])
            b_cnt = 0
            w_cnt = 0
            while queue:
                pos = queue.popleft()
                bw = queue.popleft()
                if bw == "#":
                    b_cnt += 1
                else:
                    w_cnt += 1
                for dy, dx in directions:
                    ny = dy + pos[0]
                    nx = dx + pos[1]
                    if ny == -1 or ny == h or nx == -1 or nx == w:
                        continue
                    if used[ny][nx]:
                        continue
                    bw2 = tizu[ny][nx]
                    if bw == bw2:
                        continue
                    used[ny][nx] = True
                    queue.append([ny, nx])
                    queue.append(bw2)
            ans += b_cnt * w_cnt
    print(ans)

main()