N=int(input())
a=[None]*5
for i in range(5):
    a[i] =int(input())
def minarg(l):
    nl=len(l)
    mi=10**20
    idx=-1
    for i in range(nl):
        if l[i]<mi:
            mi=l[i]
            idx=i
    return (idx,mi)
import math
i_min,a_min = minarg(a)
print(math.ceil(N/a_min) + 4)