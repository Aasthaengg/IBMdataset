a,b,c=map(int,input().split())
A=(a+b-c)**2
B=4*a*b


if A-B>0 and (c-a-b)>0:
    print('Yes')
else:
    print('No')