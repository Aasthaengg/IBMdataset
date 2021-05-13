K=int(input())
S=input()
N=len(S)
p=10**9+7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N+K ):
    fact.append((fact[-1] * i) % p) # [-1]は後ろから?
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * factinv[r] * factinv[n-r]) % p
A=0
TF=[1]
TS=[1]
for i in range(K+1):
    TF.append(TF[i]*25 %p)
    TS.append(TS[i]*26 %p)
for i in range(K+1): # Sに含まれる文字を加えるときは、必ず後ろであると考え、S[N-1]の(Sの文字を除いた)位置をiとする
    A=(A+TF[i]*TS[K-i]*cmb(i+N-1,i,p)) %p
print(A)