N, H, W = map(int, input().split())
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a >= H and b >= W:
        res += 1
print(res)