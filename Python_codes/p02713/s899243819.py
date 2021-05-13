import math
K = int(input())
gcd3 = 0
for a in range(1,K-1):
    for b in range(a+1,K):
        for c in range(b+1,K+1):
            gcd3 += math.gcd(math.gcd(a,b),c)
gcd2 = 0
for a in range(1,K):
    for b in range(a+1,K+1):
        gcd2 += math.gcd(a,b)
ans = gcd3 * 6 + gcd2 * 6 + K*(K+1)//2
print(ans)
