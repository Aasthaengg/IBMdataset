L=input()

mod=10**9+7

f=2
nf=1

for c in L[1:]:
    x=int(c)

    if x==1:
        nf=3*nf+f
        f=2*f
    else:
        nf=3*nf
    
    nf%=mod
    f%=mod

print((f+nf)%mod)
