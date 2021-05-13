from collections import Counter
import itertools
import math
def prime(n):
    ma=int(math.sqrt(n))+1
    li=[i for i in range(2,n+1)]
    primes=[]
    while li[0]<=ma:
        primes.append(li[0])
        tmp=li[0]
        li=[i for i in li if i%tmp!=0]
    primes.extend(li)
    return primes

n=int(input())
if(n<10):
    print(0)
    exit()
primes=prime(n+1)
factor=[]
for i in range(2,n+1):
    tmp=i
    for k in primes:
        while(tmp%k==0):
            tmp//=k
            factor.append(k)
values,counts=zip(*Counter(factor).most_common())
counts=list(counts)
ans=0
for i in counts:
    if(i>=74):
        ans+=1
for k in itertools.combinations(counts,2):
    if(k[0]>=2 and k[1]>=24):
        ans+=1
    if(k[0]>=4 and k[1]>=14):
        ans+=1
    if(k[0]>=24 and k[1]>=2):
        ans+=1
    if(k[0]>=14 and k[1]>=4):
        ans+=1
for k in itertools.combinations(counts,3):
    if(k[0]>=2 and k[1]>=4 and k[2]>=4):
        ans+=1
    if(k[1]>=2 and k[2]>=4 and k[0]>=4):
        ans+=1
    if(k[2]>=2 and k[1]>=4 and k[0]>=4):
        ans+=1
print(ans)