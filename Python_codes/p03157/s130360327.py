def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    H, W = (int(i) for i in input().split())
    c = [[s for s in input()] for i in range(H)]
    dist = [[-1]*W for i in range(H)]

    def bfs(c, sy, sx, H, W):
        que = deque()

        dist[sy][sx] = 0
        que.append((sy, sx))
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))
        flag = False  # 黒色マスにいるとき，True
        bla = 0
        whi = 0
        while que:
            uh, uw = que.popleft()
            if c[uh][uw] == "#":
                flag = True
                bla += 1
            else:
                flag = False
                whi += 1
            for dy, dx in d:
                next_h = uh + dy
                next_w = uw + dx
                if not(0 <= next_h < H and 0 <= next_w < W):
                    continue
                if dist[next_h][next_w] != -1:
                    continue
                if flag and c[next_h][next_w] == '#':
                    continue
                if not flag and c[next_h][next_w] == ".":
                    continue
                dist[next_h][next_w] = dist[uh][uw] + 1
                que.append((next_h, next_w))
        return bla * whi

    ans = 0
    for h in range(H):
        for w in range(W):
            if dist[h][w] != -1:
                continue
            if c[h][w] == "#":
                ans += bfs(c, h, w, H, W)
    print(ans)


if __name__ == '__main__':
    main()
