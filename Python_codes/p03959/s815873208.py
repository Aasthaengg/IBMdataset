N=int(input())
T,A=[list(map(int,input().split())) for i in range(2)]
tp,ap=0,A[0]
f=0
r=1
mod=10**9+7
x=0
if T[-1]!=A[0]:
    f=-1
for t,a in zip(T,A):
    if f==-1:
        break
    if f==0:
        if t==tp and a==ap:
            r=(r*t)%mod
        elif t==a==ap:
            f=1
        elif not (t>tp and a==ap):
            f=-1
    elif f==1:
        if t==a==ap:
            x+=1
        elif t==tp and a<ap:
            for j in range(x-1):
                r=(r*t)%mod
            f=2
        else:
            f=-1
    elif f==2:
        if t==tp and a==ap:
            r=(r*a)%mod
        elif not (t==tp and a<ap):
            f=-1
    tp,ap=t,a
if f==1:
    for j in range(x-1):
        r=(r*t)%mod
print(0 if f<1 else r)