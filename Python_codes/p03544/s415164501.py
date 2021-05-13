n=int(input())
x=0
if n==1:
    print(1)
else:
    a1=1
    a0=2
    for i in range(n-1):
        x=a1+a0
        a0=a1
        a1=x
    print(x)