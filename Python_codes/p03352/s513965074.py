x=int(input())
l=[]

if x==1:
    print(1)

else:

    for i in range(2,x+1):
        for j in range(1,x+1):
            y=j**i
            if y<=x:
                l.append(y)
            elif y>x:
                break
    print(max(l))