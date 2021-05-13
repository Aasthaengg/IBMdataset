import math
N = int(input())
LCM = N*360//math.gcd(N,360)
ans = LCM//N
print(ans)