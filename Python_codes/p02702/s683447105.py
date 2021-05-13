from collections import defaultdict

S = list(input())
S = [int(i) for i in S]
D = defaultdict(int)
mod = 2019

N = len(S)
Mlis = [0]*N
Mlis[-1] = S[-1] % mod

for i in range(N-2, -1, -1):
  Mlis[i] = (Mlis[i+1] + pow(10, N-1-i, mod) * S[i]) % mod

for i in Mlis:
  D[i] += 1

ans = D[0] + sum([i*(i-1)//2 for i in D.values()])

print(ans)