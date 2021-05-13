N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
count = 0
for n in range(N):
    if AB[n][0] >= H and AB[n][1] >= W:
        count += 1

print(count)