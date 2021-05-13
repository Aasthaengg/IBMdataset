from collections import defaultdict
factors = defaultdict(int)
N = int(input())
for i in range(2,N+1):
    target = i
    d = 2
    while d**2 <=target:
        if target % d == 0:
            factors[d] += 1
            target //= d
        else:
            d += 1

    if target != 1:
        factors[target] += 1
ans = 1
for v in factors.values():
    ans *= (v+1)
mod = 10**9 +7
print(ans%mod)
