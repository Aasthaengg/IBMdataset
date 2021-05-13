class Combination():
    def __init__(self, n, mod=10**9+7):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod

    def combination(self, n, r):
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod

    def permutation(self, n, r):
        return self.factorial(n) * self.invfactorial(n-r) % self.mod

    def factorial(self, i):
        return self.fac[i]

    def invfactorial(self, i):
        return self.invfac[i]

def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    x, y= map(int, input().split())
    if 2*x-y < 0 or 2*y-x < 0 or (2*x-y)%3 != 0 or (2*y-x)%3 != 0:
        print(0)
        return
    l = (2*x-y)//3
    k = (2*y-x)//3
    c = Combination(l+k)
    print(c.combination(l+k, l))

    


if __name__ == '__main__':
    main()