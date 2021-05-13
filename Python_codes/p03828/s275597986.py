from fractions import math
n=int(input())
#first generate all primes uptil N
def chk_prime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
primes=[]
for i in range(2,n+1):
    if chk_prime(i):
        primes.append(i)
#print(primes)
ans=1
mod=10**9+7
for i in primes:
    cnt=0
    for j in range(i,n+1,i):
        num=j
        while num%i==0:
            num//=i
            cnt+=1
    ans=(ans*(cnt+1))%mod
print(ans)
