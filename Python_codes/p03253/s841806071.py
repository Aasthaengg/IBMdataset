import math
from collections import Counter
n, m = map(int, input().split())

prime_count = Counter()
for i in range(2, math.ceil(math.sqrt(m))+1):
    while m % i == 0:
        m /= i
        prime_count[i] += 1
if m > 1:
    prime_count[int(m)] += 1

if len(prime_count) != 0:
    b_max = max([i for i in prime_count.values()])
else:
    b_max = 1

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
Mod = 10**9+7
def COMinit():
    #N_C_kのN
    for i in range(2, n+b_max):
        fac.append(fac[-1]*i%Mod)
        inv.append((-inv[Mod%i] * (Mod//i)) % Mod)
        finv.append(finv[-1] * inv[-1] % Mod)


def COM(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % Mod) % Mod

ans = 1
COMinit()
for b in prime_count.values():
    ans *= COM(n+b-1, n-1)
    ans %= Mod 

print(ans)