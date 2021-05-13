from math import ceil
T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())


#A1>=B1にする
if A1>=B1:
    pass
else:
    A1,B1=B1,A1
    A2,B2=B2,A2

D1=(A1-B1)*T1#>=0
D2=(A2-B2)*T2#?

if D1==-D2:
    print("infinity")
elif D1+D2>=0:
    print("0")
else:
    diff = abs(D1+D2)#マイからこれだけ差が開く
    if D1%diff==0:
        print(D1//diff*2)
    else:
        print(ceil(D1/diff)*2-1)
