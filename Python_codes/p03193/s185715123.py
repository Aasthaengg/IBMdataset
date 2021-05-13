N, H, W = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
s = 0
for a, b in ab:
    if a >= H and b >= W:
        s+=1

print(s, flush=True)