n=int(input())
x=[]
g=0
if n==0:
    print(0)
    exit()

if n<0:
    g=1
    n=abs(n)

if n>0:
    while n>0:
        x.insert(0,n%2)
        n=n//2
    m=len(x)
    for i in range(2*m):
        x.insert(0,0)
    m=len(x)
    for i in range(m):
        if i%2==1 and x[-i-1]==1:
            x[-i-2]+=1
        if x[-i-1]==2:
            x[-i-1]=0
            x[-i-2]+=1
    if g==1:
        for i in range(m):
            x[i]*=-1
        for i in range(m):
            if x[-i-1]==-1:
                x[-i-1]=1
                x[-i-2]+=1

    a=[]
    f=0
    for i in range(m):
        if x[i]!=0:
            f=1
        if f==1:
            a.append(x[i])
    m=len(a)
    for i in range(m):
        a[i]=str(a[i])
    print("".join(a))
