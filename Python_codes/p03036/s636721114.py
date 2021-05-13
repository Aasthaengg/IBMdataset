r, d, x2000 = map(int, input().split())

for y in range(2001, 2011):
    x2000 = x2000*r - d
    print(x2000)
