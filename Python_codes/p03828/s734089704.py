import collections

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

n = int(input())
a = []
for i in range(2,n+1):
    a += prime_factorize(i)
b = set(a)
c = collections.Counter(a)
ans = 1
for i in b:
    ans *= c[i]+1
    ans %= 10**9+7
print(ans)
