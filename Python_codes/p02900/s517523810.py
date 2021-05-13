from math import*
A,B=sorted(map(int,input().split()))
prime=[]
i=1
while i**2<=A:
    if A%i==0:
        prime.append(i)
        prime.append(A//i)
    i+=1

prime=list(set(prime))
prime.sort()
L=len(prime)
ans=[1]*L
j=1
while j<L:
    now=prime[j]
    if B%now:
        ans[j]=0
    if ans[j]==0:
        j+=1
        continue
    k=j+1
    while k<L:
        if prime[k]%now==0:
            ans[k]=0
        k+=1
    j+=1

print(sum(ans))