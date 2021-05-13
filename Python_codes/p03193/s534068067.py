N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for ab in AB:
    if ab[0] >= H and ab[1] >= W:
        ans += 1

print(ans)
