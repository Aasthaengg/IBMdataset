def query(q):
    print(q)
    a=input()
    if a=="Vacant":
        exit(0)
    return a

n=int(input())
d={}

a=query(0)
if a=="Male":
    d["Male"] = 1
    d["Female"] = 2
else:
    d["Male"] = 2
    d["Female"] = 1

a=query(n-2)
if d[a]==2:
    query(n-1)

M=n-2
m=0
while M-m>=2:
    x=(M+m+1)//2
    a=query(x)
    if (x+d[a])%2==1:
        m=x
    else:
        M=x

query(M)
query(m)
