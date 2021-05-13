a,b=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
i=0
total=0
while True:
    if b<c[i]:
        print(total)
        break
    elif i==a-1:
        if b==c[i]:
            print(total+1)
        else:
            print(total)
        break
    else:
        total+=1
        b=b-c[i]
        i+=1