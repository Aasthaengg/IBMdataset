import math
X,Y = map(int,input().split())
a = X*Y//math.gcd(X, Y)-X
if a == 0:
    print(-1)
    exit()
print(a)