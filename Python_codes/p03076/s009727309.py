a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
alist=[a,b,c,d,e]
num=0
import math
for i in range(5):
  num+=math.ceil(alist[i]/10)*10
num2=10
for i in range(5):
  if alist[i]%10!=0:
    num2=min(num2,alist[i]%10)
print(num-10+num2)