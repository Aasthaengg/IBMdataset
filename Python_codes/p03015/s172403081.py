# ABC129 E

L=input()
N=len(L)
p=10**9+7

def pow_k(x,n,p=10**9+7):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=(K*x)%p
        x=(x*x)%p
        n//=2
    return (K*x)%p


res=0
tmp=1
for i in reversed(range(N)):
    if L[N-1-i]=='1':
        res=(res+tmp*pow_k(3,i,p))%p
        tmp=(2*tmp)%p
print((res+tmp)%p) 