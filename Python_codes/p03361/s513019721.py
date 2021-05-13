H, W = map(int, input().split())
S = []
for h in range(H):
    S_h = list(input())
    S.append(S_h)

d = [-1, 1]
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            ls = []
            for i in range(2):
                for j in range(2):
                    hs = h + d[i]
                    ws = w + d[j]
                    if 0 <= hs < H and 0 <= ws < W:
                        ls.append(S[hs][w])
                        ls.append(S[h][ws])
            if '#' not in ls:
                print('No')
                exit()
print('Yes')
