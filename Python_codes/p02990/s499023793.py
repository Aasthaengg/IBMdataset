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

mod = 10**9+7
N,K = map(int,input().split())
ans_ls = [0] * K
c = Combination(N+K)
for i in range(K):
    Blocks = i+1
    #print('-----')
    #print('B:',Blocks)
    if N-K+1>=Blocks:
        Points = c.combination(N-K+1,Blocks)
    else:
        Points = 0
    #print('入れ方：',Points)
    Division = c.combination(K-1,Blocks-1)
    #print('分け方：',Division)
    ans_ls[i] = (Points*Division)%mod

for ans in ans_ls:
    print(ans)