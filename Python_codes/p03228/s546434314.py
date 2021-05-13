a, b, n = (int(i) for i in input().split())  

while n>0:
    if a % 2 ==1:
        a = (a-1)/2
        b = b + a
    else:
        a = a/2
        b = b + a
    a1=a
    b1=b
    if b % 2 ==1:
        b = (b-1)/2
        a = b + a
    else:
        b = b/2
        a = b + a
    a2=a
    b2=b
    n=n-2

if n%2==0:
    print(int(a2),int(b2))
else:
    print(int(a1),int(b1))
    
