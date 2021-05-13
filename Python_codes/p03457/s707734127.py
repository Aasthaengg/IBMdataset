n = int(input())
nt, nx, ny = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    now = t-nt
    location = abs(nx-x) + abs(ny-y)
    if location <= now and (now-location)%2 == 0:
        nt, nx, ny = t, x, y
    else:
        print('No')
        exit()
print('Yes')
