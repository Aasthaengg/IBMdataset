import math
n = int(input())
t = [int(input()) for i in range(n)]
lcm = t[0]
for h in range(1,n):
    lcm = (lcm*t[h])//math.gcd(lcm,t[h])
print(lcm)