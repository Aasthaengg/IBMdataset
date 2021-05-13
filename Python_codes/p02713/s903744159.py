from math import gcd
K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(i,K+1):
        L = gcd(i,j)
        for k in range(j,K+1):
            M = gcd(L,k)
            if i == j == k:
                ans += M
            elif i == j or j == k:
                ans += M*3
            else:
                ans += M*6
print(ans)
