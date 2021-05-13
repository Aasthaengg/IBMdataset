H, W = map(int, input().split())
h, w = map(int, input().split())
left = H*W
for i in range(h):
    left -= W
for i in range(w):
    if left <= 0:
        left = 0
    else:
        left -= H-h
print(left)