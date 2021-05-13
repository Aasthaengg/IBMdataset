def get_primes(n: int) -> list:
    sieve=[1]*n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [0] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

N=int(input())
L=get_primes(10000)
ans=[]
for i in range(len(L)):
    if L[i]%5==1:
        ans.append(L[i])
    if len(ans)==55:
        break

print(*ans[:N])