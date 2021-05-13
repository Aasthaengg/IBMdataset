H, W = map(int, input().split())
h, w = map(int, input().split())

masu = H * W
zan = masu -((h*W)+(w*(H-h)))
print(zan)