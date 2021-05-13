n,k=[int(j) for j in input().split()]
a=[int(j) for j in input().split()]
s=sum(a)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
l=make_divisors(s)
ans=1
from itertools import accumulate
for i in l[::-1]:
    ll=[]
    for j in a:
        ll.append(j%i)
    ll.sort()
    if sum(ll[:n-sum(ll)//i])<=k:
        print(i)
        exit()


