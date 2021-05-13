W, H, x, y, r = map(int, input().split())
right = x - r
left = x + r
above = y + r
below = y - r

if x < 0 or y < 0:
    print('No')
else:
    if right >= 0 and left <= W and above <= H and below >= 0:
        print('Yes')
    else:
        print('No')
