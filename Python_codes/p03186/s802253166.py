x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[-1])
n=0
if b>=c:
    n+=b+c
    print(n)
else:
    n+=2*b
    c-=b
    if a>=c:
        n+=c
        print(n)
    else:
        n+=a+1  
        print(n)
