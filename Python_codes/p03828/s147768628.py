N = int(input())

def factorize(N):
    res = {}
    for i in range(2, N):
        if i**2 > N: break
        if N % i != 0: continue
        num = 0
        while N % i == 0:
            N = int(N/i)
            num += 1
        res[i] = num
    if N>1: res[N] = 1
    return res

MOD = 10**9+7
table = [0]*(N+1)
for i in range(2, N+1):
    res = factorize(i)
    for p in res.keys():
        table[p] += res[p]
        table[p] %= MOD

ans = 1
for n in table:
    if n > 0: 
        ans *= (1+n)
        ans %= MOD

print(ans)