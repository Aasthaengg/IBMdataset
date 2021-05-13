import math

n = int(input())

c=0
for i in range(1,n+1):
    if i==1:
        c += (n*n)
        continue
    for j in range(1,n+1):
        t = math.gcd(i,j)
        if t==1:
            c += n
            continue
        for k in range(1,n+1):
            c += math.gcd(t,k)

print(c)