import sys
input=sys.stdin.readline

def make_divisors(n):
    lsls=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            lsls.append(i)
            if i!=n//i:
                lsls.append(n//i)
    lsls.sort()
    return lsls

N,K=map(int,input().split())
A=list(map(int,input().split()))

S=sum(A)
lst=make_divisors(S)

ans=1
B=[0]*N
for u in lst:
    for i in range(N):
        B[i]=A[i]%u
    B.sort()
    kkk=0
    s=0
    while kkk<N and s+B[kkk]<=K:
        s+=B[kkk]
        kkk+=1
    t=0
    for i in range(kkk,N):
        t+=u-B[i]
    if s>=t:
        ans=u

print(ans)