N,M=map(int,input().split())
A=sorted(map(int,input().split()))
B=[0]
for a in A:
    B.append(B[-1]+a)
def f(n):
    a,b=0,0
    r=N-1
    for l in range(N):
        while r>-1 and A[l]+A[r]>=n:
            r-=1
        a+=N-1-r
        b+=A[l]*(N-1-r)+B[N]-B[r+1]
    return a,b
l,r=0,10**6
x=0
while l+1<r:
    t=(l+r)//2
    a,b=f(t)
    if a<M:
        r=t
    else:
        x=max(x,t)
        l=t
a,b=f(x)
print(b-x*(a-M))