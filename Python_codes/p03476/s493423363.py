q=int(input())
n=10**5

work=[1 if i%2==1 else 0 for i in range(n+1)]
primes=[2]
lst=[0]*(n+1)
work[1]==0

for i in range(3,n,2):
    if not work[i]: continue
    primes.append(i)
    index=1
    while i*index<=n:
        work[i*index]=0
        index+=1

for i in primes[1:]:
    if (i+1)//2 in primes:
        lst[i]=1

for i in range(3,n+1):
    lst[i]+=lst[i-1]

for _ in range(q):
    left,right=map(int,input().split())
    print(lst[right]-lst[left-1])
