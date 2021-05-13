W, H, x, y, r = map(int, input().split())
print ('Yes' if x + r in range (0, W+1) and x - r in range (0, W+1) and y + r in range (0, H+1) and y - r in range(0, H + 1) else 'No')