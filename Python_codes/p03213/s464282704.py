class PrimeFactor():

    def __init__(self, n):
        """
        エラトステネス　O(N loglog N)
        """
        self.n = n
        self.table = list(range(n+1))       # 最小素因数のリスト
        self.table[2::2] = [2]*(n//2)
        for p in range(3, int(n**0.5) + 2, 2):
            if self.table[p] == p:
                for q in range(p * p, n + 1, 2 * p):
                    if self.table[q] == q:
                        self.table[q] = p

    def is_prime(self, x):
        """ 素数判定　O(1) """
        if x < 2:
            return False
        return self.table[x] == x

    def prime_factors(self, x):
        """ 素因数分解 O(logN)  (試し割りだとO(sqrt(N))) """
        res = []
        if x < 2:
            return res
        while self.table[x] != 1:
            res.append(self.table[x])
            x //= self.table[x]
        return res

    def prime_counter(self, x):
        """ 素因数分解（個数のリスト） O(logN) """
        res = dict()
        if x < 2:
            return res
        while self.table[x] != 1:
            res[self.table[x]] = res.get(self.table[x], 0) + 1
            x //= self.table[x]
        return res

#################################################################
N = int(input())
P = PrimeFactor(N)
Q = dict()
for i in range(1,N+1):
    for key, value in P.prime_counter(i).items():
        Q[key] = Q.get(key,0) + value
a, b, c, d, e = 0, 0, 0, 0, 0
for value in Q.values():
    if value >= 2: a += 1
    if value >= 4: b += 1
    if value >= 24: c += 1
    if value >= 14: d += 1
    if value >= 74: e += 1
print(b*(b-1)//2*(a-2) + c*(a-1) + d*(b-1) + e)