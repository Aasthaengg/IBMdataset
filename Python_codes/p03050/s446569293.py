
import numpy as np
def divisor(n):
    tank = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tank.append(i)
            if i!=n//i:
                tank.append(n//i)
    tank.sort()
    return tank

n = int(input())
tank = np.array(divisor(n))
res = 0
for i in range(len(tank)):
    x = tank[i] - 1
    if x!=0 and n%x==n//x:
        res += x
print(res)