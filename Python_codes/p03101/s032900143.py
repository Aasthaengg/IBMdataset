H,W = map(int,input().split())
h,w = map(int,input().split())
N = H * W
E = h * W
K = w * H
O = h * w
print((N - (E + K))+O)