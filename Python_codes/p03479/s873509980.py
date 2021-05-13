import math
x,y=map(int,input().split())
lst=[]
lst.append(x)
for i in range(2,100):
    z=0
    z=math.pow(2,i-1)*x
    if z>y:
        print(len(lst))
        break
    else:
        lst.append(z)
# print()