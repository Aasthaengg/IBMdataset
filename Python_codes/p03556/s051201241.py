import math
n = int(input())
s = 1
for i in range(2, int(math.sqrt(n)) + 1):
    if i * i <= n:
        s = i * i
print(s)
