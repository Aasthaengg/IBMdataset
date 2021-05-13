from collections import defaultdict
H, W, N = map(int, input().split())


D = defaultdict(int)
for i in range(N):
    h, w = map(int, input().split())
    h, w = h - 1, w - 1
    for dh in range(-1, 2):
        for dw in range(-1, 2):
            if not ((1 <= h + dh < H - 1) and (1 <= w + dw < W - 1)):
                continue
            D[(h + dh, w + dw)] += 1

ans = [0] * 10
for v in D.values():
    ans[v] += 1

ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
print(*ans, sep='\n')
