K = int(input())
S = input()
M = K + len(S)
alpha = "abcdefghijklmnopqrstuvwxyz"
mod = int(1e9) + 7 # <-- input modulo
maxf = 2000010           # <-- input factional limitation

def doubling(n, m, modulo=mod):
    y = 1
    base = n
    tmp = m
    while tmp != 0:
        if tmp % 2 == 1:
            y *= base
            if modulo > 0:
                y %= modulo
        base *= base
        if modulo > 0:
            base %= modulo
        tmp //= 2
    return y

def inved(a, modulo=mod):
    x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
    while l != 0:
        x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
        k, l = l, k % l
    return x % modulo

fact = [1 for _ in range(maxf+1)]
invf = [1 for _ in range(maxf+1)]

for i in range(maxf):
    fact[i+1] = (fact[i] * (i+1)) % mod
invf[-1] = inved(fact[-1])
for i in range(maxf, 0, -1):
    invf[i-1] = (invf[i] * i) % mod
  
SS = 0
bas = 1
for i in range(M, len(S)-1, -1):
  SS += (bas * invf[i] * invf[M-i]) % mod
  bas *= 25
  bas %= mod
  SS %= mod
print(SS*fact[M]%mod)
