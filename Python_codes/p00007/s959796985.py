import math
n = int(input())
a =  100000
for i in range(n):
    a =  a*1.05
    if a%1000 == 0:
        a = a
    else:
        a = (a//1000*1000+1000)
print(math.floor(a))
