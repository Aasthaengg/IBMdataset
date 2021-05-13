n=int(input())

mod=10**9+7

def prime_fact(x):
    fact=[]
    for i in range(2, int(x**(0.5))+1):
        while x%i==0:
            fact.append(i)
            x//=i
    if x!=1:
        fact.append(x)
    if not fact:
        fact=[x]
    return fact

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

era=eratosthenes(n)
d={}
for key in era:
    d[key]=0

for i in range(2,n+1):
    prime_list=prime_fact(i)
    for prime in prime_list:
        d[prime]+=1

ans=1
for key in d:
    ans*=(d[key]+1)%mod

print(ans%mod)