from math import factorial

n,k = map(int,input().split())
mod = 10**9+7

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))#組み合わせ

for i in range(1,k+1):
    if n-k < i-1:
        print(0)
    else:
        iti = combinations_count(k-1,i-1)
        ni = combinations_count(n-k+1,i)
        iti%=mod;ni%=mod
        print(iti*ni%mod)