import numpy as np

N, X, T = map(int, input().split())

for n in range(1,1000):
    if n>=N/X:
        break
    n+=1

print(T*n)
