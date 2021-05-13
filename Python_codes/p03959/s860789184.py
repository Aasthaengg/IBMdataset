mod = 1000000007
n= int(input())
t= list(map(int,input().split()))
a= list(map(int,input().split()))
tb = [-1]*n
pre=-1
for i in range(n):
    if i==0:tb[i]=1
    else:
        if pre!=t[i]:tb[i]=1
    pre=t[i]
ab = [-1]*n
post=-1
for i in range(n-1,-1,-1):
    if i==n-1:ab[i]=1
    else:
        if post!=a[i]:ab[i]=1
    post=a[i]
er = False
if a[0]!=t[-1]:er=True
else:
    b=1
    for i in range(n):
        if tb[i]==1 or ab[i]==1:
            if tb[i]==1 and ab[i]==1:
                if t[i]==a[i]:pass
                else:
                    er=True
                    break
            else:
                if tb[i]==1:
                    if a[i]<t[i]:
                        er=True
                        break
                elif ab[i]==1:
                    if a[i]>t[i]:
                        er = True
                        break
        else:
            m = min(a[i],t[i])
            b = ((b% mod) * (m % mod)) % mod
if er:print(0)
else:print(b)
