from collections import defaultdict

H, W, N = list(map(int, input().split()))
YX = [list(map(int, input().split())) for _ in range(N)]

memo = defaultdict(int)
for y, x in YX:
    y -= 1; x -= 1
    for i in range(9):
        memo[y - 1 + i//3, x - 1 + i%3] += 1

ans = [0] * 10
for y, x in memo:
    if 0 < x < W-1 and 0 < y < H-1:
        ans[memo[y, x]] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans)
print(*ans)