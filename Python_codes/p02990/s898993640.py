mod = 10**9 + 7

fact_range = 2010
facts = [1] * (fact_range + 1)
for i in range(0, fact_range):
    facts[i+1] = facts[i] * (i + 1) % mod

ifacts = [1] * (fact_range + 1)
ifacts[fact_range] = pow(facts[fact_range], mod - 2, mod)
for i in range(fact_range, 0, -1):
    ifacts[i-1] = ifacts[i] * i % mod

def comb(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return facts[n] * ifacts[n-k] % mod * ifacts[k] % mod

n, k = map(int, input().split())
m = n - k
for i in range(1, k + 1):
    print(comb(k - 1, i - 1) * comb(m + 1, i) % mod)

