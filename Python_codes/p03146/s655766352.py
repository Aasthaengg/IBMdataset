s=int(input())

if s==4 or s==2 or s==1:
    print(4)
    

else:
    l=[]
    for i in range(10**6+1):
        l.append(s)
        if l.count(4)>2:
            break
        elif s%2==0:
            s=s//2
        else:
            s=3*s+1
    x=l.index(4)

    l=l[x+1:]
    y=l.index(4)

    print(y+x+2)