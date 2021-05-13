from math import ceil

R, G, B, n = map(int, input().split())
rm = ceil(n / R)
gm = ceil(n / G)
bm = ceil(n / B)
ans = 0
for r in range(rm+1):
    for g in range(gm+1):
        x = n-(r*R+g*G)
        if x >= 0:
            ans += (x%B == 0)

print(ans)
