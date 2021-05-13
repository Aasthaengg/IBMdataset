import math
n = int(input())
res = 0
for i in range(1,n+1):
    keta = int(math.log10(i))+1
    if(keta % 2 == 1):
        res += 1
print(res)