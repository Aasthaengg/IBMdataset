def primes(n):#nまでの素数を列挙
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**(0.5)+1)):
        if not is_prime[i]:
            continue
        for j in range(i*2,n+1,i):
            is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]], is_prime
li_p, is_prime = primes(10**5+1)
li_p.reverse()
for i in li_p:
    if  is_prime[int((i+1)/2)]:
        continue
    else:
        is_prime[i] = False
res = [0] * (10**5+1)
for i in range(10**5+1):
    if i == 0:
        continue
    if is_prime[i]:
        res[i] = res[i-1] + 1
    else:
        res[i] = res[i-1]
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    if l>0:
        print(res[r] - res[l-1])
    else:
        print(res[r])