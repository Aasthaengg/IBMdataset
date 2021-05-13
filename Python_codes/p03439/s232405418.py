n=int(input())
print(0)
a=input()
d={}
if a=="Vacant":
    exit(0)
elif a=="Male":
    d["Male"] = 1
    d["Female"] = 2
else:
    d["Male"] = 2
    d["Female"] = 1
print(n-2)
a=input()
if a=="Vacant":
    exit(0)
elif d[a]==2:
    print(n-1)
    exit(0)

M=n-2
m=0

while M-m>=2:
    x=(M+m+1)//2

    print(x)
    a=input()
    if a=="Vacant":
        exit(0)

    if (x+d[a])%2==1:
        m=x
    else:
        M=x
        
    x=(M+m+1)//2

print(M)
a=input()
if a=="Vacant":
    exit(0)
print(m)
a=input()
if a=="Vacant":
    exit(0)
