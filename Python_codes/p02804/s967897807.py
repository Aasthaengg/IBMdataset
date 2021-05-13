import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np
 
N,K = map(int, readline().split())
A = np.array(read().split(), np.int64)
MOD = 10 ** 9 + 7
 
def cumprod(A, MOD = MOD):
    L = len(A); Lsq = int(L**.5+1)
    A = np.resize(A, Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        A[:,n] *= A[:,n-1]; A[:,n] %= MOD
    for n in range(1,Lsq):
        A[n] *= A[n-1,-1]; A[n] %= MOD
    return A.ravel()[:L]

def make_fact(U, MOD = MOD):
    x = np.arange(U, dtype = np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact,fact_inv
 
fact, fact_inv = make_fact(10 ** 5 + 100)
 
A.sort()
coef = (fact[K-1:N] * fact_inv[K-1] % MOD * fact_inv[0:N-K+1] % MOD)[::-1]
 
answer = ((A[::-1][:N-K+1] - A[:N-K+1]) * coef % MOD).sum() % MOD
print(answer)