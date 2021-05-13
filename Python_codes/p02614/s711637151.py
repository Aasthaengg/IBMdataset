import itertools

H, W, K = map(int, input().split())
S = [input() for i in range(H)]
ans = 0
for si in itertools.product([0, 1], repeat=H):
    for sj in itertools.product([0, 1], repeat=W):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if si[i] or sj[j]:
                    continue
                if S[i][j] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
