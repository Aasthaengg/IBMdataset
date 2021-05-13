import math
X=int(input())
print(360*X//math.gcd(360,X)//X)