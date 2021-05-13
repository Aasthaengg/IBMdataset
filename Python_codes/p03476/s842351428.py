import numpy as np
def make_prime(U):
    is_prime = np.zeros(U,np.bool)
    is_prime[2] = 1
    is_prime[3::2] = 1
    M = int(U**.5)+1
    for p in range(3,M,2):
        if is_prime[p]:
            is_prime[p*p::p+p] = 0
    return is_prime, is_prime.nonzero()[0]

p=set(make_prime(10**5)[1])
lst=[0]*(10**5+2)
cnt=0
for i in range(100001):
    if i in p and (i+1)//2 in p:
        cnt+=1
    lst[i]=cnt
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(lst[r]-lst[l-1])