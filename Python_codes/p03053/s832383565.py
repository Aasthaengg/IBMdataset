from collections import deque
def main():
    H,W = map(int, input().split())
    road = [[False]*W for _ in range(H)]
    arrived = [[False]*W for _ in range(H)]
    que = deque([]) # BFS:appendleftとpopでキュー
    origWhite = 0
    for i in range(H):
        c = input()
        for j in range(W):
            if c[j]=='.':
                road[i][j] = True
                origWhite += 1
            else:
                que.append((i,j))
                arrived[i][j] = True

    if origWhite<=0:
        print(0)
        return

    directions = [(1,0),(0,1),(-1,0),(0,-1)] # 東西南北に移動可能
    depth = [[0]*W for _ in range(H)]
    while que:
        x1,y1 = que.pop()
        for dx,dy in directions:
            x2,y2 = x1+dx,y1+dy
            # 枠外
            if x2<0 or H<=x2 or y2<0 or W<=y2:
                continue
            # 壁
            if not road[x2][y2]:
                continue
            # 探索済み
            if arrived[x2][y2]:
                continue
            que.appendleft((x2,y2))
            arrived[x2][y2] = True
            origWhite -= 1
            depth[x2][y2] = depth[x1][y1]+1
            if origWhite<=0:
                print(depth[x2][y2])
                return


main()
