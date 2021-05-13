t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

d1 = (a1-b1)*t1
d2 = (b2-a2)*t2

if d1 == d2:
    print('infinity')
 
if d1 * (d2 - d1) < 0:
    print(0)

if d1*(d2-d1)>0:
    if d1%(d1-d2)==0:
        print((d1//(d2-d1))*2)
    else:
        print((d1//(d2-d1))*2+1)