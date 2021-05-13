def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
def judge(d):
    R=[]
    for a in A:
        R.append(a%d)
    R.sort()
    R_rev=[]
    for r in R:
        R_rev.append(d-r)
    R_acc=[0]*(n+1); R_rev_acc=[0]*(n+1)
    for i in range(n):
        R_acc[i+1]=R_acc[i]+R[i]
    for i in reversed(range(n)):
        R_rev_acc[i]=R_rev_acc[i+1]+R_rev[i]
    tmp=float('inf')
    for i in range(n+1):
        tmp=min(tmp,max(R_acc[i],R_rev_acc[i]))
    return tmp<=k

n,k=map(int,input().split())
A=tuple(map(int,input().split()))
s=sum(A)
D=make_divisors(s)
ans=1
for d in D:
    if judge(d):
        ans=d
print(ans)