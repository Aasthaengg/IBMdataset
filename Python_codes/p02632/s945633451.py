K = int(input())
S = input()
S = len(S)


mod = 10**9 + 7

b = mod-2
blis = []
c = 0
while b >0:
  if b & 1 == 1:
    blis.append(c)
  c += 1
  b >>= 1

def modinv(a):
  if a == 1:
    return 1
  else:
    res = 1
    li = []
    for _ in range(c):
      li.append(a%mod)
      a = a*a%mod
    for item in blis:
      res = res *li[item] %mod
    return res

from collections import deque

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, K + S + 1):
  fact.append((fact[-1] * i) % mod)
  if i < K+2:
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

factinv_k = deque(factinv[:K+1])
fact_ks = deque(fact[S-1:])


list26 = deque([1])
list25 = deque([1])
now26 = 26
now25 = 25
for k in range(K):
  list25.append(now25)
  list26.append(now26)
  now25 = now25*25%mod
  now26 = now26*26%mod


ans = 0
for k in range(K+1):
  now = list26.pop()
  now = now * list25.popleft() % mod
  now = now * fact_ks.popleft() % mod
  now = now * factinv_k.popleft() %mod
  ans += now
  ans %= mod


ans *= modinv(fact[S-1])
ans %= mod
print(ans)
