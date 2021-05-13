W, H, x, y, r = [int(x) for x in input().split()]
print('No' if x - r < 0 or y - r < 0 or x + r > W or y + r > H else 'Yes')