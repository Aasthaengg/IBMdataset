import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

T1,T2 = MI()
A1,A2 = MI()
B1,B2 = MI()

if A1*T1 + A2*T2 == B1*T1 + B2*T2:
    print('infinity')
    exit()

if A1*T1 + A2*T2 > B1*T1 + B2*T2:
    A1,B1 = B1,A1
    A2,B2 = B2,A2

if A1 < B1:
    print(0)
    exit()

if ((A1-B1)*T1) % (B1*T1+B2*T2-A1*T1-A2*T2) != 0:
    print(((A1-B1)*T1)//(B1*T1+B2*T2-A1*T1-A2*T2)*2+1)
else:
    print(((A1-B1)*T1)//(B1*T1+B2*T2-A1*T1-A2*T2)*2)
