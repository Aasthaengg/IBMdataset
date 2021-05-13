class Osa_k:
    def __init__(self, n_max):
        self.n_max = n_max
        self.min_factor = min_factor = list(range(n_max + 1))
        min_factor[2::2] = [2] * (n_max // 2)
        min_factor[3::6] = [3] * ((n_max + 3) // 6)
        for i in range(5, int(n_max ** .5) + 1, 2):
            if min_factor[i] == i:
                for j in range(i*i, n_max + 1, i):
                    if min_factor[j] == j:
                        min_factor[j] = i

    def __call__(self, n):
        min_factor = self.min_factor
        t = []
        while n > 1:
            if t and t[-1][0] == min_factor[n]:
                t[-1][1] += 1
            else:
                t.append([min_factor[n], 1])
            n //= min_factor[n]
        res = 1
        for _, i in t:
            res *= i + 1
        return res

P = Osa_k(10**7)
print(sum(i * P(i) for i in range(1, int(input()) + 1)))
