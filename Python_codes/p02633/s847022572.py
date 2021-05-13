X=int(input())
import math
a=360*X//math.gcd(360,X)
print(a//X)