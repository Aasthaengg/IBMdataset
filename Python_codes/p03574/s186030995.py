H, W = map(int, input().split())
S = []
for h in range(H):
    S_h = list(input())
    S.append(S_h)

d = [-1, 0, 1]
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        else:
            count = 0
            for i in range(3):
                for j in range(3):
                    hs = h + d[i]
                    ws = w + d[j]
                    if 0 <= hs < H and 0 <= ws < W and S[hs][ws] == '#':
                        count += 1
                    else:
                        continue
            S[h][w] = str(count)

ans_row = [''.join(S[h]) for h in range(H)]
print('\n'.join(ans_row))