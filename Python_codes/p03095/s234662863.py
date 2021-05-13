n = int(input())
S = str(input())

d = {}
for i in range(n):
    if S[i] not in d:
        d[S[i]] = 1
    else:
        d[S[i]] += 1

mod = 10**9+7
ans = 1
for v in d.values():
    ans *= (v+1)
    ans %= mod
ans -= 1
print(ans%mod)
