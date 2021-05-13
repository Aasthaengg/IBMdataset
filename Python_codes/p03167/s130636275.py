MOD = 10**9 + 7


def main():
    from collections import deque
    H, W = (int(i) for i in input().split())
    c = [input() for i in range(H)]
    dist = [[-1]*W for i in range(H)]

    def bfs_2d(sy=0, sx=0):
        que = deque()

        dist[sy][sx] = 1
        que.append((sy, sx))
        d = ((0, 1), (1, 0))
        while que:
            uh, uw = que.popleft()
            for dy, dx in d:
                next_h = uh + dy
                next_w = uw + dx
                if not(0 <= next_h < H and 0 <= next_w < W):
                    continue
                if dist[next_h][next_w] != -1:
                    dist[next_h][next_w] += dist[uh][uw]
                    dist[next_h][next_w] %= MOD
                    continue
                if c[next_h][next_w] == '#':
                    continue
                dist[next_h][next_w] = dist[uh][uw]
                dist[next_h][next_w] %= MOD
                que.append((next_h, next_w))

    bfs_2d()
    print(dist[H-1][W-1] if dist[H-1][W-1] != -1 else 0)


if __name__ == '__main__':
    main()
