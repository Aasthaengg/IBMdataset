class Sieve:
    # Sieve of Eratosthenes
    def __init__(self, n):
        f = [0]*(n+1)
        primes = list()
        f[0] = f[1] = -1
        for i in range(2,n+1):
            if f[i]:
                continue
            primes.append(i)
            f[i]=i
            for j in range(i*i, n+1, i):
                if not f[j]:
                    f[j] = i
        self.f = f
        self.primes = primes
    def isPrime(self, x):
        return self.f[x] == x
    def factorList(self, x):
        res = list()
        while x > 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res
    def factor(self, x):
        fl = self.factorList(x)
        if len(fl) == 0:
            return list()
        res = [[fl[0], 0]]
        for p in fl:
            if res[-1][0] == p:
                res[-1][1] += 1
            else:
                res.append([p, 1])
        return res

sv= Sieve(10000)

n=int(input())
ans=1
d=dict()
for i in range(2,n+1):
    f=sv.factor(i)

    for p,cnt in f:
        try:
            d[p]+=cnt
        except:
            d[p]=cnt

for p,cnt in d.items():
    ans*=(cnt+1)
    ans%=(10**9+7)

print(ans)


