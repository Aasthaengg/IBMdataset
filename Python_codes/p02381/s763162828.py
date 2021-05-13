import math
while True:
    a=0
    A=0
    b=0
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    S=sum(s)
    m=S/n
    for i in range(n):
        b=(s[i]-m)**2
        a=a+b
    A=a/n
    C=math.sqrt(A)
    print(C)
