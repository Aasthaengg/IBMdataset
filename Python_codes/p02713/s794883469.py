K=int(input())

def gcd(x,y):
    if x<y:
        temp=x
        x=y
        y=temp
    if x%y==0:
        return y
    else:
        nx=y
        ny=x%y
        return gcd(nx,ny)
ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        g=gcd(a,b)
        for c in range(1,K+1):
            ans+=gcd(g,c)

print(ans)