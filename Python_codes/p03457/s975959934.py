N = int(input())
t, x, y = 0, 0, 0
for i in range(N):
    nt, nx, ny = map(int, input().split())
    km = abs(nx-x) + abs(ny-y)
    if km > (nt-t) or (km - (nt-t)) % 2 == 1:
        print("No")
        exit(0)
    t, x, y = nt, nx, ny
print("Yes")