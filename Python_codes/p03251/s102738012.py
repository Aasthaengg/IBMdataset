n, m, x, y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))

for z in range(x+1, y+1):
    if max(lx) < z and min(ly) >= z:
        print('No War')
        exit()

print('War')