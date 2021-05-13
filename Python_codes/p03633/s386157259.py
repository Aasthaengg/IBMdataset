import math
n = int(input())
t = [int(input()) for _ in range(n)]
if n == 1:
    print(t[0])
    exit()
a = t[0]*t[1]//math.gcd(t[0],t[1])
for i in range(2, n):
    a = t[i]*a//math.gcd(t[i],a)
print(a)