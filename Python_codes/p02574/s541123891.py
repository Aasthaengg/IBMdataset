N=int(input())
A=list(map(int,input().split()) )
import math

se = A[0]
for i in range(1,N):
    se = math.gcd(se,A[i])
set_wise = se==1

NMAX = 10**6+2
divisors = [i for i in range(NMAX+1)]
p=2
while p*p <=NMAX:
    if divisors[p]==p:
        for r in range(2*p,NMAX+1,p):
            if divisors[r]==r:
                divisors[r]=p
    p+=1
    
from collections import defaultdict
def soinsu_osak(to_devide):
    d = defaultdict(int)
    while to_devide>1:
        d[divisors[to_devide]]+=1
        to_devide //= divisors[to_devide]
    return list(d.keys())

been=[0]*NMAX
pair_wise=True
f=False
for aa in A:
    soinsu = soinsu_osak(aa)
    for s in soinsu:
        if been[s]==0:
            been[s]=1
        else:
            pair_wise=False
            f=True
            break
    if f:
        break

if pair_wise:
    print("pairwise coprime")
elif set_wise:
    print("setwise coprime")
else:
    print("not coprime")