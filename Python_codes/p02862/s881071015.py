mod=10**9+7
x,y=map(int,input().split())

X,Y=(2*y-x)//3,(2*x-y)//3
if X<0 or Y<0 or (x+y)%3!=0:print(0);exit()


def cmb(n,r,mod):
    if r<0 or r>n:return 0
    return g1[r]*g2[r]%mod


n=X+Y
k=max(X,Y)
g1=[1,n]
g2=[1,1]
inverse=[0,1]

for i,j in enumerate(range(n-1,((n-k+1)-1),-1)):
    i=i+2
    g1.append((g1[-1]*j)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1]%mod))

print(cmb(n,k,mod))