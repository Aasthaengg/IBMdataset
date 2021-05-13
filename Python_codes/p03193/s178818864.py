N, H, W = map(int, input().split())
ABlist = [list(map(int, input().split())) for _ in range(N)]
counter = 0
for a, b in ABlist:
    if a >= H and b >= W:
        counter += 1

print(counter)
