H, W = map(int, input().split())
h, w = map(int, input().split())

delrow = h*W
delcol = w*H
dup = h*w
print(H*W - delrow - delcol + dup)