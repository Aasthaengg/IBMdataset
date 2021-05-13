import sys 

k = int(input())
x=0;y=0
if k%2==0:
    x=int(k/2);y=int(k/2)
else:
    x=int(k/2)+1;y=int(k/2)
print(x*y)
