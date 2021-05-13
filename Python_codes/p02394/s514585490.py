W,H, x, y, r = [int(i) for i in input().split()]

if x - r < 0 or x + r > W:
    print('No')
else:
    print('No') if y - r < 0 or y + r > H else print('Yes')