N, H = map(int,input().split())
L = []
maxi = 0
for _ in range(N):
    a,b = map(int,input().split())
    maxi = max(maxi, a)
    L.append((a,b))
L = [x for x in L if x[1] > maxi]
L = sorted(L,key = lambda x:x[1],reverse=True)
throw = 0
for i in range(len(L)):
    throw += L[i][1]
    if throw >= H:
        print(i + 1)
        quit()
from math import ceil
print(ceil((H - throw) / maxi) + len(L))
    
