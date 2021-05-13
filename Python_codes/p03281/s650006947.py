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

    def prime_counter(self, x):
        """
        素因数分解（個数のリスト） O(logN)
        {素因数: 個数}　の形で返す
        """
        res = dict()
        if x < 2:
            return res
        while self.table[x] != 1:
            res[self.table[x]] = res.get(self.table[x], 0) + 1
            x //= self.table[x]
        return res

    def divisors_counter(self, x):
        """ 約数の個数　O((logN)^2) """
        res = 1
        for value in self.prime_counter(x).values():
            res *= (value+1)
        return res

N = int(input())
P = PrimeFactor(N)
res = 0
for i in range(1,N+1,2):
    if P.divisors_counter(i)==8:
        res += 1
print(res)