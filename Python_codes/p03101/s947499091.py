H, W = map(int, input().split())
h, w = map(int, input().split())
result = H*W - (h*w+h*(W-w)+w*(H-h))
print(str(result))