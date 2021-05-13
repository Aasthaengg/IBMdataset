T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
d1 = (A1-B1)*T1
d2 = (A2-B2)*T2

if d1*d2>0:
    print(0)
    exit()

if d1<0:
    d1 *= -1
    d2 *= -1

if d1+d2>0:
    print(0)
    exit()

if d1+d2==0:
    print('infinity')
    exit()

t = -d2-d1

if d1%t==0:
    print(d1//t*2)
else:
    print(d1//t*2+1)