import math

N = int(input())
ck = math.floor(N/4)
dk = math.floor(N/7)

c = 4
d = 7
result = False

for i in range(ck+1):
    for j in range(dk+1):
        if (N == c * i + d * j):
            result = True
            break

if result == True:
    print('Yes')
else:
    print('No')
