class RollingHash():
    def __init__(self,s):
        self.n=n=len(s)
        self.b=b=129
        self.M=M=2**61-1
        self.f=f=[1]*(n+1)
        self.h=h=[0]*(n+1)
        for i,c in enumerate(s.encode()):
            f[i+1]=f[i]*b%M
            h[i+1]=(h[i]*b+c)%M
    def get(self,l,r):
        return(self.h[r]-self.h[l]*self.f[r-l])%self.M
n=int(input())
s=RollingHash(input())
for i in range(1,n):
    d={}
    for j in range(0,n-i+1):
        k=s.get(j,j+i)
        if k in d:
            if d[k]+i<=j:
                break
        else:
            d[k]=j
    else:
        print(i-1)
        break