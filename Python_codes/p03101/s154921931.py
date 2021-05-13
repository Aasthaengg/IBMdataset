H, W = map(int, input().split())
h, w = map(int, input().split())

H_white = H - h
W_white = W - w

print(H_white * W_white)