h, w, K = map(int, input().split())
lc = []
for _ in range(h):
    lc += list(input().split())

ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        cnt = 0
        for k in range(h):
            for l in range(w):
                if i >> k & 1:
                    continue
                if j >> l & 1:
                    continue
                if lc[k][l] == '#':
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)