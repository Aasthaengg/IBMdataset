from collections import deque

H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    temp = []
    for j in range(W):
        temp.append(s[j])
    S.append(temp)

ret = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '?':
            q = deque()
            q.appendleft((i, j))
            white = 0
            black = 0
            while q:
                h, w= q.pop()
                color = S[h][w]
                if color == '?':
                    continue
                elif color == '#':
                    black += 1
                else:
                    white += 1
                S[h][w] = '?'
                cand = [(h+1, w), (h-1, w), (h, w+1), (h, w-1)]
                for hc, wc in cand:
                    if 0 <= hc < H and 0 <= wc < W and (S[hc][wc] not in [color, '?']):
                        q.appendleft((hc, wc))

            ret += black * white

print(ret)
