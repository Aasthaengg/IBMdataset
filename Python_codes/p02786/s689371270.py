import math, copy
h=int(input())

cnt=0
a=copy.copy(h)
while a>1:
    a=math.ceil(a/2)
    cnt+=1

if h==2**(cnt):
    print(2**(cnt+1)+-1)
else:
    print(2**(cnt)+-1)