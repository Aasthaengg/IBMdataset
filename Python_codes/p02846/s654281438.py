T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

if A1>B1:
    A1,A2,B1,B2 = B1,B2,A1,A2
D1 = B1-A1
D2 = B2-A2

if D1*T1 + D2*T2 > 0:
    print(0)
    exit()
if D1*T1 + D2*T2 == 0:
    print('infinity')
    exit()

p = D1*T1
q = -D2*T2
d = q-p
k = p//d
b = int(q*k == p*(k+1))
print(1 + k*2 - b)