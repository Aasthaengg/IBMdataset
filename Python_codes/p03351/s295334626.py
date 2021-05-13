a, b, c, d = map(int, input().split())

dir_ab = abs(a - b)
dir_bc = abs(b - c)
dir_ca = abs(c - a)

if dir_ca <= d or (dir_ab <= d and dir_bc <= d):
    print('Yes')
else:
    print('No')
