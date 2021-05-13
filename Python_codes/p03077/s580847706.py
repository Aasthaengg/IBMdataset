from math import ceil
n = int(input())
A = []
for i in range(5):
    A.append(int(input()))
print(ceil(n/min(A))+4)