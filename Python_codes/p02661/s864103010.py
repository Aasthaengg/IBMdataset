n,*t=map(int,open(0).read().split())
A=sorted(t[0::2])
B=sorted(t[1::2])
if n%2==0:
    kl=n//2-1
    kr=n//2
else:
    kl=n//2
    kr=n//2
lm,lM=A[kl],A[kr]
rm,rM=B[kl],B[kr]
L,R=0,0
if n%2==0:
    L=lm+lM
    R=rm+rM
    a=R-L+1
else:
    a=rm-lm+1
print(a)