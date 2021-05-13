H, W = map(lambda x: int(x), input().split())
h, w = map(lambda x: int(x), input().split())

print(H*W - (h*w + h*(W-w) + w*(H-h)))