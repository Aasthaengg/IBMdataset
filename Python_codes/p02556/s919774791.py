n = int(input())

zmax = 0
zmin = 10**10
wmax = -10**10
wmin = 10**10

for i in range(n):
    x, y = map(int, input().split())
    zref = x + y
    wref = x - y
    zmax = max(zmax, zref)
    zmin = min(zmin, zref)
    wmax = max(wmax, wref)
    wmin = min(wmin, wref)

ans = max(zmax - zmin, wmax - wmin)
print(ans)