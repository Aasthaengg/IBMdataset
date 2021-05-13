from math import gcd
X = int(input())
Y = (X*360)//gcd(X,360)
print(Y//X)