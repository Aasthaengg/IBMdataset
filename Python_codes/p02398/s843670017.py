n=0
(a,b,c) = [int(i) for i in input().split()]
if a > c:
    print(0)

else:
    if b > c:
        b=c
    for i in range(a,b+1):
        if c%i==0:
            n=n+1
        
    print(n)