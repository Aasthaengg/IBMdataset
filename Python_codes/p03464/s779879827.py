K=int(input())
A=list(map(int,input().split()))

def g(n):
    for a in A:
        n=n-n%a
    return n

a_max=max(A)
l=1
r=2+K*a_max
while r-l>1:
    m=(l+r)//2
    if g(m)>=2:
        r=m
    else:
        l=m
l0=r

l=1
r=2+K*a_max
while r-l>1:
    m=(l+r)//2
    if g(m)<=2:
        l=m
    else:
        r=m
r0=l

if l0>r0:
    print(-1)
else:
    print(l0,r0)