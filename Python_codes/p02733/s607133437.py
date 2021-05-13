from itertools import combinations

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

C = [[0] * (W + 1) for _ in range(H + 1)]
for h in range(H):
    wc = 0
    for w in range(W):
        wc += (S[h][w] == '1')
        C[h + 1][w + 1] = C[h][w + 1] + wc

ans = 2000
for cuth in range(H):
    for comb in combinations([h for h in range(1, H)], cuth):
        comb = [0] + list(comb) + [H]
        wi, cutw = 0, 0
        for w in range(W):
            if max([C[comb[i]][w + 1] - C[comb[i]][wi] - C[comb[i - 1]][w + 1] + C[comb[i - 1]][wi] for i in range(1, len(comb))]) > K:
                if wi == w:
                    cutw = 2000
                wi, cutw = w, cutw + 1
        ans = min(ans, cuth + cutw)

print(ans)
