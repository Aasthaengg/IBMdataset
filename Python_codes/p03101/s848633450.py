H,W = map(int,input().split())
h,w = map(int,input().split())

Area = H*W
Area -= W*h
Area -= (H-h)*w

print(Area)