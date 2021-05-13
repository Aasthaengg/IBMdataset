import numpy as np
n = int(input())
A, B = [], []
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

x = np.median(A)
y = np.median(B)
if n%2==0:
    print(int((y-x)/0.5+1))
else:
    print(int(y-x+1))