
class Solve:
    def __init__(self):
        self.N, self.K = [int(i) for i in input().split()]
        self.W = [int(input()) for i in range(self.N)]

        self.a = max(self.W)-1  # >= 0; False
        self.b = sum(self.W)  # <= 10**9; True

    def check(self, P):
        k, p, W = 1, P, [w for w in self.W]
        for w in W:
            if p >= w:
                p -= w
            elif P >= w and k < self.K:
                k, p = k+1, P-w
            else:
                return False
        return True

    def solve(self):
        while self.b - self.a > 1:
            m = (self.a + self.b) // 2
            if self.check(m):
                self.b = m
            else:
                self.a = m
        return self.b

print(Solve().solve())