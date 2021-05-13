import math
k=int(input())
a=100
c=0
while a<k:
    a+=a//100
    c+=1
print(c) 