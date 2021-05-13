n=int(input())
# p^74 p^2q^24 p^2q^4r^4 p^4q^14 
# 2^74 q=2,3,5           q=2,3,5,7,
#3 5 5
#75,5 15,3 25,3 5 5 
from collections import defaultdict
memo=defaultdict(lambda:-1)

def f(x):
    if memo[x]!=-1:return memo[x]
    ret=0;temp=n
    while temp:
        temp//=x
        ret+=temp
    memo[x]=ret
    return ret
ans=0
primes=[2,3]
for i in range(5,101,6):
    for p in primes:
        if i%p:continue
        break
    else:primes.append(i)
    i+=2
    for p in primes:
        if i%p:continue
        break
    else:primes.append(i)
di=[i**2 for i in primes]
qu=[j**2 for j in di]
for p in primes:
    if f(p)>=74:ans+=1
    else:break
def g(a,b):
    global ans
    for p in primes:
        if f(p)>=a:
            for q in primes:
                if f(q)>=b:
                    if q!=p:ans+=1
                    else:continue
        else:break
    return 0
g(2,24)
g(4,14)

for q in range(len(qu)):
    for r in range(q+1,len(qu)):
        a,b=qu[q],qu[r]
        if not (f(primes[q])>=4 and f(primes[r])>=4):continue
        for i,d in enumerate(di):
            if d**2 not in {a,b} and f(primes[i])>=2:ans+=1
print(ans)