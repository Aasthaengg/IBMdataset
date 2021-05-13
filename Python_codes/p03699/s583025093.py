a=int(input())
b=[0]*a
import sys
for i in range(a):
    b[i]=int(input())
b.sort()
c=sum(b)
if c%10==0:
    for i in range(a):
        if b[i]%10!=0:
            c=c-b[i]
            print(c)
            sys.exit()
    print(0)
else:
    print(c)
