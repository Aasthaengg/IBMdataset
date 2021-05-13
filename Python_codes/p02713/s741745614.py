def gcd(p,q):
    while q != 0:
        r = p % q
        p = q
        q = r
    return p
k = int(input())
a = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for k in range(1,k+1):
            a += gcd(gcd(i,j),k)
print(a)