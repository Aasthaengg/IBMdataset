a,b=input().split()
a=int(a)
b=int(b)
i=0
sum=0
if b==1:
    print(0)
else:
    while True:
        if i==0:
            b=b-a
            sum+=1
            i+=1
        elif b<=0:
            print(sum)
            break
        else:
            b=b-a+1
            sum+=1
            i+=1