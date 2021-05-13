n=int(input())
x=input()
chk0=chk1=chk2=0
b=x.count("1")
if b==1 and x=="1":
    print(0)
    exit()
elif b==1:
    for i in range(n):
        if i==n-1: print(2)
        elif x[i]=="0": print(1)
        else: print(0)
    exit()
for i,j in enumerate(x[::-1]):
    if j=="1":
        chk1+=pow(2,i,b+1)
        if b>1: chk2+=pow(2,i,b-1)
        else: chk2=0
l=[]
for i,j in enumerate(x[::-1]):
    if b: a1=pow(2,i,b+1)
    else: a1=1
    if b>1: a2=pow(2,i,b-1)
    else: a2=1
    if j=="0":
        t=chk1+a1
    else:
        if b>1: t=chk2+b-1-a2
        else: t=0
    ans,f=0,1
    while t:
        if f:
            if j=="0": t%=(b+1)
            else: t%=(b-1)
            f=0
        else:
            t%=bin(t).count("1")
        ans+=1
    l.append(ans)
for i in l[::-1]:
    print(i)