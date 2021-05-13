
import math

x=input()
y=input()
flag=True
if(x[0]!=y[2]):
    flag=False
elif(x[2]!=y[0]):
    flag=False
elif(x[1]!=y[1]):
    flag=False
if(flag):
    print("YES")
else:
    print("NO")