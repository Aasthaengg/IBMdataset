N, M = [int(_) for _ in input().split()]
xyz = []
for _ in range(N):
    xyz.append([int(_) for _ in input().split()])

ans = -1
for i in range(8):
    sx = -(i >> 2 & 1) or 1
    sy = -(i >> 1 & 1) or 1
    sz = -(i >> 0 & 1) or 1
    xyz.sort(key=lambda v: sx * v[0] + sy * v[1] + sz * v[2], reverse=True)
    x, y, z = 0, 0, 0
    for a in xyz[:M]:
        x += a[0]
        y += a[1]
        z += a[2]
    ans = max(ans, abs(x) + abs(y) + abs(z))
print(ans)
