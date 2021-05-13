mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input().rstrip('\n'))

    ans = 0
    seen = [[0] * W for _ in range(H)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for h0 in range(H):
        for w0 in range(W):
            if seen[h0][w0] == 0:
                que = deque([(h0, w0)])
                seen[h0][w0] = 1
                black = white = 0
                while que:
                    h, w = que.popleft()
                    if grid[h][w] == "#":
                        black += 1
                    else:
                        white += 1
                    for dh, dw in d:
                        h_new, w_new = h+dh, w+dw
                        if 0 <= h_new < H and 0 <= w_new < W:
                            if seen[h_new][w_new] == 0:
                                if grid[h][w] != grid[h_new][w_new]:
                                    que.append((h_new, w_new))
                                    seen[h_new][w_new] = 1
                ans += black * white
    print(ans)


if __name__ == '__main__':
    main()
