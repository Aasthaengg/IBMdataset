import math

x = int(input())

k = int(math.sqrt(x))

l = [1]

for i in range(2, k+1):
    j = 2
    while i ** j <= x:
        l.append(i ** j)
        j += 1

print(max(l)) 