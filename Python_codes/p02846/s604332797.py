import numpy

t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

v1=b1-a1
v2=b2-a2

x1=v1*t1
x2=v2*t2
di = abs(abs(x2)-abs(x1))
if numpy.sign(x1)==numpy.sign(x2):
    print(0)
elif abs(x2)<abs(x1):
    print(0)
elif abs(x1)==abs(x2):
    print("infinity")
else:
    if abs(x1)%di==0:
        print(abs(int(2*(x1/di))))
        #di = abs(x2)-abs(x1)
    else:
        print(abs(int(2*(x1//di)+1)))
