def isPrime(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    if x%2 == 0:
        return 0
    ir=int(x**(0.5))+1
    for i  in range(3,ir,2) :
        if x%i == 0:
            return 0
    return 1

n=int(input())

p=[]
for i in range(n+1):
    if isPrime(i):
        p.append(i)

pp=[0]*len(p)
for ni in range(2,n+1):
    for pi in range(len(p)):
        pcnt=0
        nn=ni
        while nn>0:
            if nn%p[pi]==0:
                nn=nn//p[pi]
                pcnt+=1
            else:
                break
        pp[pi]=pp[pi]+pcnt
    
mod=10**9+7
ppp=1
for pi in range(len(p)):
    if pp[pi]!=0:
        ppp=ppp*(pp[pi]+1)%mod
print(ppp)