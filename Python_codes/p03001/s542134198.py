W, H, x, y = map(int, input().split())

if x == W*0.5 and y == H*0.5:
    print(H*W*0.5, 1)
else:
    print(H*W*0.5, 0)