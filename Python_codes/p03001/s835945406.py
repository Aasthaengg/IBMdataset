W, H, x, y = map(int, input().split())
v = x/W
h = y/H
if v and h == 0.5 :
    print(W*H/2, 1)
else:
    print(W*H/2, 0)