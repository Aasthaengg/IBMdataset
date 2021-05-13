import sys
n = int(input())
a = []

if (n==1):
    print(1)
    sys.exit()

def prime_factorize(n,a):
    while n%2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f*f <= n:
        if n%f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for i in range(2,n+1):
    a = prime_factorize(i,a)

a.sort()
c = []
count = 1
for i in range(1,len(a)):
    if(a[i-1]!=a[i]):
        c.append(count)
        count = 1
    else:
        count += 1
c.append(count)

ans = 1
for i in range(0,len(c)):
    ans *= (c[i]+1)
print(ans % 1000000007)