import fractions
import sys
sys.setrecursionlimit(10**9)

MOD = 1000000007  # type: int
INF=10**20

class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict



class Counting():
    def __init__(self,maxim,mod):
        maxim += 1

        self.mod = mod
        self.fact = [0]*maxim
        self.fact[0] = 1
        for i in range(1,maxim):
            self.fact[i] = self.fact[i-1] * i % mod

        self.invfact = [0]*maxim
        self.invfact[maxim-1] = pow(self.fact[maxim-1],mod-2,mod)
        for i in reversed(range(maxim-1)):
            self.invfact[i] = self.invfact[i+1] * (i+1) % mod


    def nCk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[r] * self.invfact[n-r] % self.mod

    def nPk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[n-r] % self.mod

        


def solve(N: int, A: "List[int]", B: "List[int]"):

    both_zero = 0
    a_zero = 0
    b_zero = 0
    
    counter = Counter()
    for i in range(N):
        a,b=A[i],B[i]   

        if a * b == 0:
            if a == 0 and b == 0:
                both_zero += 1
                continue
            elif a == 0:
                a,b = 0,1
            else:
                a,b = -1,0

        
        gcd = fractions.gcd(a,b)
        a //= gcd
        b //= gcd

        # (a,b): -はaの方に寄せる
        if a < 0 and b < 0:
            a *= -1
            b *= -1
        if a < 0 and b > 0:
            pass

        if a > 0 and b < 0:
            a *= -1
            b *= -1
        
        counter.add((a,b))

    
    seen = set()
    cannot = 0
    counter = counter.get_dict()

    ans = 1
    for e,count in counter.items():
        a,b = e
        if e in seen: continue
        # print(e)
    
        if a > 0:
            b *= -1
        else:
            a *= -1

        if (b,a) in seen: continue

        if (b,a) in counter:
            count2 = counter[(b,a)]

            ans *= pow(2,count,MOD) + pow(2,count2,MOD) - 1
        else:
            ans *= pow(2,count,MOD)
        
        ans %= MOD
        seen.add((b,a))
        # print(ans)
        
    # ans *= pow(2,a_zero,MOD) + pow(2,b_zero,MOD) - 1
    ans %= MOD

    ans += both_zero - 1
    ans %= MOD

    print(ans)


    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)



if __name__ == "__main__":
    main()
