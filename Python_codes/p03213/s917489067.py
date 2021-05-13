N = int(input())
c = [0 for i in range(101)]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for i in range(2,N+1):
    factors = prime_factorize(i)
    for factor in factors:
        c[factor] += 1
c = [e+1 for e in c]

ans = 0
#75 = 5*5*3
more75 = len(list(filter(lambda x:x>=75,c)))
more25 = len(list(filter(lambda x:x>=25,c)))
more15 = len(list(filter(lambda x:x>=15,c)))
more5 = len(list(filter(lambda x:x>=5,c)))
more3 = len(list(filter(lambda x:x>=3,c)))

ans += more75
if more25:
    ans += more25*(more3-1)
if more15:
    ans += more15*(more5-1)
if more5 >= 2 and more3 >= 3:
    ans += (more3-2)*(more5*(more5-1))//2
print(ans)

