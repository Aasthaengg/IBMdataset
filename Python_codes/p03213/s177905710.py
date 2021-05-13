import math

n=int(input())
D={}

def DictAppend(n,d):
    if n in d:
        d[n]+=1
    else:
        d[n]=1

for i in range(1,n+1):
    if i==1:
        continue
    now=i
    while now%2==0:
        now//=2
        DictAppend(2,D)
    p=3
    while p<=math.sqrt(i):
        while now%p==0:
            now//=p
            DictAppend(p,D)
        p+=2
        if now==1:
            break
    if now>math.sqrt(i):
        DictAppend(now,D)

P=[74,24,14,4,2]
C=[0,0,0,0,0]
for d in D:
    for i in range(5):
        if D[d]>=P[i]:
            C[i]+=1

ans=0
ans+=C[0] #a**74
if C[4]>1:
    ans+=C[1]*(C[4]-1) #a**24 * b**2
if C[3]>1:
    ans+=C[2]*(C[3]-1) #a**14 * b**4
if C[4]>2:
    ans+=C[3]*(C[3]-1)//2*(C[4]-2) #a**4 * b**4 * c**2
print(ans)