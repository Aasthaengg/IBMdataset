from collections import deque


def main():
    H, W = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#' or visited[h][w] == 1:
                continue
            n_white, n_black = 0, 0
            que = deque()
            que.append((h, w))
            while len(que) > 0:
                ch, cw = que.pop()
                if visited[ch][cw] == 1:
                    continue
                visited[ch][cw] = 1
                if S[ch][cw] == '.':
                    n_white += 1
                else:
                    n_black += 1
                for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_h, next_w = ch + dh, cw + dw
                    if 0 <= next_h < H and 0 <= next_w < W and \
                        S[ch][cw] != S[next_h][next_w] and \
                        visited[next_h][next_w] == 0:
                        que.append((next_h, next_w))
            ans += n_white * n_black
    print(ans)


if __name__ == '__main__':
    main()