import math as m

n = int(input())
x = m.ceil(n/1.08)
if(m.floor(x*1.08) == n):
    print(x)
else:
    print(":(")