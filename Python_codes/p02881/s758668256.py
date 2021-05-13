import math
N = int(input())
Nruto = math.sqrt(N)
Nruto = math.floor(Nruto)
for i in range(Nruto+1, 0, -1):
    if N % i == 0:
        a = N//i
        b = i
        break
print(a+b-2)
