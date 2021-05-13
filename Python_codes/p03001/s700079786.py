W,H,X,Y = map(int,input().split())
a = W*H/2
b = 1 if X*2==W and Y*2==H else 0
print(a,b)