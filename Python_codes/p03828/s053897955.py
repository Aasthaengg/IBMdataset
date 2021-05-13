import math

n = int(input())
mod = 10**9+7

def eratosthenes(n):
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

if n==1:
    print(1)
    exit()

era = eratosthenes(n)

dict = {}
for i in range(n):
    num = i+1
    while num!=1:
        for j in era:
            while num%j==0:
                num/=j
                if j in dict:
                    dict[j]+=1
                else:
                    dict[j]=1

ans = 1
for i in dict:
    ans = ans*(dict[i]+1)%mod

print(ans)
