def change(A,B,C):
    a=B/2+C/2
    b=A/2+C/2
    c=A/2+B/2
    return a,b,c
A,B,C=map(int,input().split())
a=A
b=B
c=C
if (A%2==1)|(B%2==1)|(C%2==1):
    print(0)
else:
    count=0
    while True:
        A,B,C=change(A,B,C)
        count+=1
        if (A%2==1)|(B%2==1)|(C%2==1):
            print(count)
            break
        elif (a==A)&(b==B)&(c==C):
            print(-1)
            break