n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
d={}
mod=10**9+7
def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        r=-1
        while r!=0:
            r=x%y
            x=y
            y=r
        return x
    else:
        r=-1
        while r!=0:
            r=y%x
            y=x
            x=r
        return y
z=0
for i in range(n):
    a,b=ab[i]
    if a==0 and b==0:
        z+=1
        continue
    if a==0:
        b=1
        y=(a,b)
        if y in d:
            d[y]+=1
        else:
            d[y]=1
        continue
    if b==0:
        a=1
        y=(a,b)
        if y in d:
            d[y]+=1
        else:
            d[y]=1
        continue
    x=gcd(a,b)
    a//=x
    b//=x
    if a<0:
        a*=-1
        b*=-1
    y=(a,b)
    if y in d:
        d[y]+=1
    else:
        d[y]=1
ans=1
re={}
for t,v in d.items():
    if t in re:
        continue
    a,b=t
    c=0
    if (b,-a) in d:
        c+=d[(b,-a)]
        re[(b,-a)]=1
    if (-b,a) in d:
        c+=d[(-b,a)]
        re[(-b,a)]=1
    ans*=(2**v-1+2**c-1+1)
    ans%=mod
ans-=1
ans+=z
ans%=mod
print(ans)
