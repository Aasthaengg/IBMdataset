import numpy as np

def multi_input():
    return map(int, input().split())

A, B, M = multi_input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
C = [list(map(int, input().split())) for i in range(M)]

mn = np.inf
for x, y, c in C:
    mn = min(mn, a[x-1]+b[y-1]-c)
mn = min(mn, min(a)+min(b)) 
print(mn)