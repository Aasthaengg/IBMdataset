import math
n=int(input())
i=0
E=100
while(i<n):
    E=E*1.05
    E=math.ceil(E)
    i=i+1

print(E*1000)
