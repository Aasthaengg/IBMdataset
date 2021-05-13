import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

K = ri()
S = rs()

class CombMod:
    def __init__(self, N):
        self.fact = [1]
        self.rfact = [1]
        for i in range(1, N+1):
            self.fact.append(self.fact[i-1]*i % mod)
            self.rfact.append(pow(self.fact[i], mod-2, mod))

    def comb(self, n, k):
        return self.fact[n]*self.rfact[k]*self.rfact[n-k] % mod

N = len(S)
cm = CombMod(K+N)

pows = [1]
pows2 = [1]
p = 1
p2 = 1
for i in range(K+1):
	p = (p * 25) % mod
	p2 = (p2 * 26) % mod
	pows.append(p)
	pows2.append(p2)
#print(pows)
ans = 0
for i in range(K+1):
	#ans += cm.comb(K+N-i-1, N-1) * pow(26, i, mod) * pow(25, K-i, mod)
	ans += cm.comb(K+N-i-1, N-1) * pows2[i] * pows[K-i]
	ans = ans % mod
print(ans)
