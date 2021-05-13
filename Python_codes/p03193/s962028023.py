N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

count = 0
for ab in AB:
    a = ab[0]
    b = ab[1]
    if a >= H and b >= W:
        count += 1
print(count)