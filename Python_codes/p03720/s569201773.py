import numpy as np

n, m = map(int, input().split(' '))

array = np.zeros(n)

for i in range(m):
    a, b = map(int, input().split(' '))
    array[a-1] += 1
    array[b-1] += 1
    
for number in array:
    print(int(number))