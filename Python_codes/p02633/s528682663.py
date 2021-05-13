from math import gcd
X = int(input())

lm = (X*360)//gcd(X,360)
print(lm//X)