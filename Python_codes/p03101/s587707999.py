H,W = map(int,input().split())
h,w = map(int,input().split())
TOTAL = H * W
total = (W * h + H * w)-h*w
result = TOTAL - total
print(result)