n,a,b,*p,=map(int,open(0).read().split())
A,B,C=0,0,0
for i in p:
    if i<=a:
        A+=1
    elif i<=b:
        B+=1
    else:
        C+=1
print(min(A,B,C))