import sys
input = sys.stdin.readline

N, M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for a in [-1, 1]:
    for b in [-1, 1]:
        for c in [-1, 1]:
            xyz.sort(key=lambda t: a*t[0]+b*t[1]+c*t[2])
            xs, ys, zs = 0, 0, 0
            
            for x, y, z in xyz[:M]:
                xs += x
                ys += y
                zs += z
            
            ans = max(ans, abs(xs)+abs(ys)+abs(zs))

print(ans)