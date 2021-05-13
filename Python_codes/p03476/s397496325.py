import sys
input=sys.stdin.readline
q=int(input())

primes=[True]*100001
primes[0]=False
primes[1]=False

for i in range(2,100001):
    if primes[i]:
        for j in range(2,100000//i+1):primes[i*j]=False

sim2017=[0]*100001
for i in range(3,100001,2):
    sim2017[i]=sim2017[i-2]+(1 if primes[i] and primes[(i+1)//2] else 0)

for i in range(q):
    l,r=map(int,input().split())
    print(sim2017[r]-sim2017[l-2])
    

