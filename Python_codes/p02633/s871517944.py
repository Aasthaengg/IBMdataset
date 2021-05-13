
import math
n = int(input())

circle = n * 360 // math.gcd(360,n)

print(circle // n)
