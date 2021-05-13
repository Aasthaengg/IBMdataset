N=int(input())

factors = {num: 0 for num in range(2, N+1)}

def factorization(n, factors):
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            factors[i] += cnt

    if temp!=1:
        arr.append([temp, 1])
        factors[temp] += 1

    if arr==[]:
        arr.append([n, 1])
        factors[n] += 1

    return factors

for num in range(2, N+1):
    factors = factorization(num, factors)
    
ans = 1
MOD = 10**9+7
for num in range(2, N+1):
    ans *= (factors[num] + 1) % MOD
    ans %= MOD
print(ans % MOD)