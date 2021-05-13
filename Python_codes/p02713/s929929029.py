def gcd(p, q):
    if (p%q == 0):
        return q
    return gcd(q, p%q)
K = int(input())
result = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            result += gcd(gcd(i, j), k)
print(result)