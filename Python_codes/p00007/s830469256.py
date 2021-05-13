import math
j = 100
for _ in range(int(input())):
    j = math.ceil(j * 1.05)
print(j * 1000)
