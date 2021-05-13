import math
N = int(input())

res = int(input())

for i in range(N-1):
    t = int(input())
    gcd = math.gcd(res,t)
    res = (res//gcd)*(t//gcd)*gcd
print(res)