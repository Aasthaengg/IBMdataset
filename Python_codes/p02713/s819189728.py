import math
K = int(input()) + 1
s = 0
for i in range(1,K):
    for j in range(1,K):
        ij = math.gcd(i, j)
        for k in range(1,K):
            s += math.gcd(ij, k)
print(s)

