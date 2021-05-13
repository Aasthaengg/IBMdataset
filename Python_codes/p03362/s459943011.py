def get_sieve_of_eratosthenes_new(n):
    import math
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

primelist=get_sieve_of_eratosthenes_new(55555)

N=int(input())
ans=[]
count=0
i=0
while count<N:
    if primelist[i]%5==1:
        ans.append(primelist[i])
        count+=1
    i+=1
print(*ans)
