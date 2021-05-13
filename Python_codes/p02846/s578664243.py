T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())
X=(B1-A1)*T1
Y=(B2-A2)*T2
if X>0:
    X=-X
    Y=-Y
if X+Y<0:
    print(0)
elif X+Y==0:
    print("infinity")
else:
    A=(-X)//(X+Y)
    B=(-X)%(X+Y)
    if B!=0:
        print(2*A+1)
    else:
        print(2*A)
