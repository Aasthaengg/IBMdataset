def primes(n):
    ass = []
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if not is_prime[i]:
            continue
        #i**2から始めてOK
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ass.append(i)
    return ass

p_list = primes(55555)
ans = []
for p in p_list:
    if p%5 == 1:
        ans.append(p)

n = int(input())

print(' '.join(map(str,ans[:n])))
