W, H, x, y = map(int, input().split())

print('{:.6f}'.format(float(W*H/2)), end=" ")

if float(x) == W/2 and float(y) == H/2:
    print(1)
else:
    print(0)