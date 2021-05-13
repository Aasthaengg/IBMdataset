# coding: utf-8
from math import gcd

def getPrime(x):
    num_list=[i for i in range(2,x+1)]
    prime_list=[]
    D=[x+1 for i in range(x+1)]
    
    while num_list[0]<x**(1/2):
        p=num_list.pop(0)
        prime_list.append(p)
        for i in range(len(num_list)):
            if num_list[i]%p==0:
                if D[num_list[i]]>p:
                    D[num_list[i]]=p
        num_list = [e for e in num_list if e % p != 0]
    
    prime_list = prime_list + num_list
    for i in range(len(prime_list)):
        D[prime_list[i]] = prime_list[i]
    D[0]=1
    D[1]=1
    return D

N = int(input())
A = list(map(int,input().split()))

if max(A) == 1:
    print("pairwise coprime")
    exit()

D = getPrime(max(A))

pc_flg = True

x = A[0]
for i in range(N):
    x = gcd(x,A[i])

prime_flg=[False for i in range(10**6+1)]

for i in range(N):
    num = A[i]
    primes = []
    while True:
        p = D[num]
        num = num//p
        primes.append(p)
        if num == 1:
            break
    for j in set(primes):
        if not(prime_flg[j]):
            prime_flg[j] = True
        else:
            if j != 1:
                pc_flg = False


if pc_flg:
    print("pairwise coprime")
elif x==1:
    print("setwise coprime")
else:
    print("not coprime")