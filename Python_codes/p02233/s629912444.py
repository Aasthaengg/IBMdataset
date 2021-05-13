n=int(input())
a,b=1,1
if n<=1:
    print(1)
else:
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(c)
