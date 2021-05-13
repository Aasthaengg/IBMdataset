class Sieve: 
    
    def __init__(self, n=1):
        self.f = [0 for _ in range(n+1)]
        self.f[0] = -1
        self.f[1] = -1
        self.primes = []
        for i in range(2, n+1):
            if self.f[i]:
                continue
            self.primes.append(i)
            self.f[i] = i
            for j in range(i*i, n+1, i):
                if not self.f[j]:
                    self.f[j] = i
    
    def isPrime(self, x):
        return self.f[x] == x
    
    def factorList(self, x):
        res = []
        while x != 1:
            res.append(self.f[x])
            x //= self.f[x]
        return res
    
    def factor(self, x):
        fl = self.factorList(x)
        if not len(fl):
            return []
        res = [[fl[0], 0]]
        for p in fl:
            if res[-1][0] == p:
                res[-1][1] += 1
            else:
                res.append([p, 1])
        return res

n = int(input())

s = Sieve(55555)
ans = []
i = 11
while len(ans) < n:
    if s.isPrime(i):
        ans.append(i)
    i += 10
print(*ans)