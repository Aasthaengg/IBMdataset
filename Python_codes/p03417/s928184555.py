N,M=map(int,input().split())
l=[N,M]
l.sort()
buf=0
f=0
c=0
if l[0]==1:
    if l[1]==1:
        print("1")
    else:
        print(l[1]-2)
else:   #l[0]>1
    print((l[0]-2)*(l[1]-2))


