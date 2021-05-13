class ModCombination:
    """
    nCk (mod m)を扱うクラス
    """

    def __init__(self, mod, n_max):
        """
        イニシャライザ
        予め 1~nの階乗と階乗の逆元を計算しておく
        :param mod: 法
        :param n_max: nの最大値(100,000で約1秒)
        """
        self.mod = mod
        self.n_max = n_max
        self.facts = [1, 1]
        self.inverses = [None, 1]
        self.fact_inverses = [1, 1]

        for i in range(2, self.n_max + 1):
            self.facts.append(self.facts[i - 1] * i % self.mod)
            # self.inverses.append(mod_inverse(i, self.mod))
            self.inverses.append(
                self.mod - self.inverses[self.mod % i] *
                (self.mod // i) % self.mod
            )
            self.fact_inverses.append(
                self.fact_inverses[i - 1] * self.inverses[i] % self.mod
            )

    def mod_combination(self, n, k):
        """
        nCk (mod m)を計算する
        :param n: n
        :param k: k
        :return: nCk (mod m)
        """
        if k > n:
            raise ValueError
        elif k == n:
            return 1
        elif k == 0:
            return 1

        denominator = self.fact_inverses[k] * self.fact_inverses[n - k] % self.mod
        return self.facts[n] * denominator % self.mod


X, Y = map(int, input().split(' '))
MOD = 10 ** 9 + 7
N_MAX = max(X, Y)

ans = 0
comb = ModCombination(mod=MOD, n_max=N_MAX)
for a in range(N_MAX + 1):
    if a > X or 2 * a > Y:
        break
    dx = X - a
    dy = Y - (2 * a)
    if dx != 2 * dy:
        continue
    b = dy

    ans += comb.mod_combination(a + b, a)
    ans %= MOD

print(ans)
