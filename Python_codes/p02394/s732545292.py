W, H, x, y, r = map(int, input().split())
print('Yes' if x - r >= 0 and x + r <= H and y - r >= 0 and y + r <= H else 'No')