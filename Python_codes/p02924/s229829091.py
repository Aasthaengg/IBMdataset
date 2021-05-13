import math
n = int(input())
dum1 = (n-1 + 1) * ((n-1)//2)
if (n-1) % 2 == 0:
    print(dum1)
else:
    print(dum1+math.ceil((n-1)/2))