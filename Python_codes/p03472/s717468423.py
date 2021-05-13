N, H = map(int,input().split())
L = []
maxi = 0
for _ in range(N):
    a,b = map(int,input().split())
    maxi = max(maxi, a)
    L.append(b)
 
#L = sorted([x for x in L if x > maxi])[::-1]
L = sorted(filter(lambda x:x>maxi,L))[::-1]
throw = 0
for i in range(len(L)):
    throw += L[i]
    if throw >= H:
        print(i + 1)
        quit()
from math import ceil
print(ceil((H - throw) / maxi) + len(L))
    

