H, W = map(int, input().split())
h, w = map(int, input().split())
print(max(H-h,0)*max(W-w,0))