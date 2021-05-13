from math import gcd
x = int(input())
# kx が 360 度になるような最小の k が答え
k = x * 360 // gcd(x, 360)
print(k // x)