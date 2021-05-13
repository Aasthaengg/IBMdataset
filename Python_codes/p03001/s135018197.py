W, H, x, y = map(int, input().split())

print( W*H/2, 1 if (x+x == W) and (y+y == H) else 0)