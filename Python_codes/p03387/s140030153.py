a,b,c=map(int,input().split())
if a%2==b%2 and b%2==c%2:
    print((2*max(a,b,c)-(a+b+c-max(a,b,c)))//2)
else:
    if a%2==b%2:
        d=a
        a=c
        c=d
    elif a%2==c%2:
        d=a
        a=b
        b=d
    b+=1
    c+=1
    print(1 + (2*max(a,b,c)-(a+b+c-max(a,b,c)))//2)