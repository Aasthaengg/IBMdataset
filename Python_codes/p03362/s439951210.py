import math
def prime(n):
    max=int(math.sqrt(n))
    li=[i for i in range(2,n+1)]
    primes=[]
    while li[0]<=max:
        primes.append(li[0])
        tmp=li[0]
        li=[i for i in li if i%tmp!=0]
    primes.extend(li)
    return primes
N=int(input())
li=[i for i in prime(1382) if i%5==1]
print(*li[:N])