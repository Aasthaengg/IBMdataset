#b
a=[None]*5
for i in range(5):
    a[i] =int(input())

import math

suma = sum(math.ceil(aa/10)*10 for aa in a)
ans=10**10
for i in range(5):
    ans = min(ans,a[i] + suma - math.ceil(a[i]/10)*10 )
print(ans)