from itertools import permutations
import math

n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split(' '))
    x.append(xi)
    y.append(yi)

list = [i for i in range(n)]

total = 0
for i in permutations(list):
    norm = 0
    for j in range(n-1):
        X = x[i[j+1]] - x[i[j]]
        Y = y[i[j+1]] - y[i[j]]
        norm += math.sqrt(X**2 + Y**2)
    total += norm
print(total/math.factorial(n))
