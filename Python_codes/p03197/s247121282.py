import numpy as np
n = int(input())
flag = False
for i in range(n):
    a = int(input())
    if a %2 == 1:
        flag = True

if flag:
    print("first")
else:
    print("second")