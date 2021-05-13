W, H, N = map(int, input().split())
region_w = [0, W]
region_h = [0, H]

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        region_w[0] = max(region_w[0], x)
    elif a == 2:
        region_w[1] = min(region_w[1], x)
    elif a == 3:
        region_h[0] = max(region_h[0], y)
    else:
        region_h[1] = min(region_h[1], y)

if (region_w[0] >= region_w[1]) or (region_h[0] >= region_h[1]):
    print(0)
else:
    print((region_w[1]-region_w[0])*(region_h[1]- region_h[0]))
