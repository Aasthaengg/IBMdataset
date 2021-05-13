import math
N = int(input())
sum1 = 0
for a in range(1,N+1):
    for b in range(1,N+1):
        for c in range(1,N+1):
            sum1 += math.gcd(c,math.gcd(a,b))
print(sum1)