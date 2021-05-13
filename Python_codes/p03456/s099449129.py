import math
n = int(input().replace(' ',''))
M = math.ceil(math.sqrt(n))

for i in range(1,M+1):
    if i**2 == n:
        print('Yes')
        exit()

print('No')
