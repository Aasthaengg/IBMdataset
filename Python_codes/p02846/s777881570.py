t1,t2=[int(j) for j in input().split()]
a1,a2=[int(j) for j in input().split()]
b1,b2=[int(j) for j in input().split()]
c1,c2=a1-b1,a2-b2
d1,d2=c1*t1,c2*t2
if d1>0:
    d1=-d1
    d2=-d2
if d1+d2<0:
    print(0)
elif d1+d2==0:
    print("infinity")
else:
    print(2*(-d1//(d2+d1))+[0,1][int(bool(-d1%(d2+d1)))])