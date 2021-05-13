import math

n,k = map(int,input().split(' '))
p = 0

for i in range(1,n+1):
    if i > k:
        x = 0
    else:
        x = math.ceil(math.log2(k/i))
    p += 1/((2**x)*n)

print(p)