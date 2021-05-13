H, W, K = map(int, input().split())
rsum = [[0] * (W + 1)]
for _ in range(H):
    rsum.append([0])
    tot = 0
    for c, v in enumerate(map(int, input())):
        tot += v
        rsum[-1].append(tot + rsum[-2][c + 1])
ans = 10 ** 10
for i in range(1 << H):
    hcuts = [0]
    for j in range(H - 1):
        if i & (1 << j):
            hcuts.append(j + 1)
    hcuts.append(H)
    vcuts = [0]
    ok = True
    for c in range(1, W + 1):
        for b in range(2):
            max_w = 0
            for h in range(1, len(hcuts)):
                max_w = max(
                    max_w,
                    rsum[hcuts[h]][c]
                    - rsum[hcuts[h - 1]][c]
                    - rsum[hcuts[h]][vcuts[-1]]
                    + rsum[hcuts[h - 1]][vcuts[-1]],
                )
            if max_w > K:
                if b:
                    ok = False
                    break
                vcuts.append(c - 1)
        if not ok:
            break
    if not ok:
        continue
    vcuts.append(W)
    ans = min(ans, len(hcuts) - 2 + len(vcuts) - 2)
print(ans)
