H, W = map(int, input().split())
S = [input() for _ in range(H)]
t = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = True
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            for h1, w1 in t:
                h2 = h1 + h
                w2 = w1 + w
                if H <= h2 or W <= w2 or h2 < 0 or w2 < 0:
                    continue
                if S[h2][w2] == '#':
                    break
            else:
                ans = False
print('Yes' if ans else 'No')

