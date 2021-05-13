H,W = map(int,input().split())
h,w = map(int,input().split())

A = H * W #マスの数
A = A - (h * W) #行を黒塗り
A = A - ((H - h) * w) #列を黒塗り

print(A)
