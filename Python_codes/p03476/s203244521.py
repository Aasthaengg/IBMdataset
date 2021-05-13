import math
q=int(input())

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

prime=[0]*(10**5+1)
prime_lst=get_sieve_of_eratosthenes(10**5)
for i in prime_lst:
    prime[i]+=1

a=[0]*(10**5+1)
for i in range(3,10**5+1):
    if prime[i]==1 and prime[(i+1)//2]==1:
        a[i]+=1

for i in range(1,10**5+1):
    a[i]=a[i-1]+a[i] 

for i in range(q):
    l,r=map(int,input().split())
    print(a[r]-a[l-1])