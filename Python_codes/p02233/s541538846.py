x=int(input())
a=1
b=1
i=1
if x==0:
    print(1)
elif x==1:
    print(1)

else:
    while i<=x-1:
        c=a+b
        a=b
        b=c
        i+=1
    print(c)
