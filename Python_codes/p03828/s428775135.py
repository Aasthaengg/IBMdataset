from collections import Counter
N = int(input())
factors = []
for i in range(N):
    T = N-i
    d = 2
    while d**2<=T:
        if T%d==0:
            factors.append(d)
            T//=d
        else:
            d+=1
    if T!=1:
        factors.append(T)
factors = Counter(factors)
ans = 1
for v in factors.values():
    ans *= (v+1)
mod = 10**9 +7
print(ans%mod)