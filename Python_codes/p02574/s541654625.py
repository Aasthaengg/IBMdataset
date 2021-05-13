import random
import math
N=int(input())
A=[int(i) for i in input().split()]
isPrime=[1 for i in range(10**6+1)]
isPrime[0]=0;isPrime[1]=0
Pfact=[[] for i in range(10**6+1)]
for i in range(10**6+1):
    if isPrime[i]==0:
        continue
    Pfact[i].append(i)
    for j in range(2*i,10**6+1,i):
        isPrime[j]=0
        Pfact[j].append(i)

Prime=[]
for i in range(10**6+1):
    if isPrime[i]:
        Prime.append(i)
def ispairwisecoprime():
    X=set()
    t=0
    for i in range(N):
        for j in Pfact[A[i]]:
            if j in X:
                return False
                exit()
            else:
                X.add(j)
    return True
if ispairwisecoprime():
    print("pairwise coprime")
else:
    G=A[0]
    for i in range(1,N):
        G=math.gcd(G,A[i])
    if G==1:
        print("setwise coprime")
    else:
        print("not coprime")
