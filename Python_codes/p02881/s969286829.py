import math
n = int(input())
p = 10 ** 12
m = math.floor(math.sqrt(n))

for i in range(1,m + 1):
    if n % i == 0:
        j = n // i
        p = min(p,i-1+j-1)

print(p)