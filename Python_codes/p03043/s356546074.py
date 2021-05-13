import math

n,k = (int(x) for x in input().split())
p = 0
for i in range(1,n+1):
    a = max([math.ceil((math.log2(k/i))),0])
    p += 1/(n*(2**a))

print(p)
