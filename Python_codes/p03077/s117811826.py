import math

n = int(input())
lis = []
for _ in range(5):
    lis.append(int(input()))
    
print(math.ceil(n/min(lis)+4))