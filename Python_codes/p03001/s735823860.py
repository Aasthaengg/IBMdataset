def LI():
    return list(map(int, input().split()))


W, H, x, y = LI()
if x*2 == W and y*2 == H:
    total = 1
else:
    total = 0
print(W*H/2, total)
