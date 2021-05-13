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

N = int(input())

l = []
for n in range(N):
  l.extend(prime_factorize(n+1))

c = collections.Counter(l)

ans = 1
for v in c.values():
  ans *=(v+1)
  ans %= 1000000007
print(ans)