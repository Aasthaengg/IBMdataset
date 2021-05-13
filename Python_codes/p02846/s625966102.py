T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

C1 = (A1-B1)*T1
C2 = (A2-B2)*T2

if C1+C2==0:
    print('infinity')
elif C1*(C1+C2)>0:
    print(0)
else:
    if abs(C1)%abs(C1+C2)==0:
        print(abs(C1)//abs(C1+C2)*2)
    else:
        print(abs(C1)//abs(C1+C2)*2+1)