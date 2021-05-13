H,W=map(int,input().split())
h,w=map(int,input().split())
A=H*W
B=h*W
C=w*(H-h)
print(A-B-C)