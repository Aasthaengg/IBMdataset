import numpy as np
N = int(input())
num = list(map(int,input().split()))
for i in range(1, N+1):
    num[i-1] -= i
numbers = np.array(num)
b = int(round(np.median(numbers)))
numbers-= b
number = np.abs(numbers)
print(number.sum())