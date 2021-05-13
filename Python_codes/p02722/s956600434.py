import collections

N = int(input())

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

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


c = collections.Counter(prime_factorize(N-1))
ans = 1
lis = make_divisors(N)

for i in c.values():
    ans *= i+1
ans -=1

for i in lis:
    if i==1:continue
    tmp = N
    while tmp%i==0:
        tmp //= i
    if tmp%i==1:
        ans+=1

print(ans)
