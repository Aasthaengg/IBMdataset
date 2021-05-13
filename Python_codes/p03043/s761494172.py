import math
n,k = list(map(int,input().split()))
p = 0 

for i in range(1, n+1):
    if i<k:
        t = math.ceil(math.log2(k/i))
        p +=(1/n)*(1/2)**t
    else:
        p += 1/n
print(p)