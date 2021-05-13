arr = input().split(' ')
(W, H, x, y, r) = tuple([int(x) for x in arr])

if ((x - r) < 0):
    print('No')
elif ((x + r) > W):
    print('No')
elif ((y - r) < 0):
    print('No')
elif ((y + r) > H):
    print('No')
else:
    print('Yes')