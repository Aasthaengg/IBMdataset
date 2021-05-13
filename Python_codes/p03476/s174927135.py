q = int (input())

def pr(n):
    L = [1]*(n+1)
    L[0] = 0
    L[1] = 0
    for i in range(2,n+1):
        for j in range(2*i,n,i):
            L[j] = 0
    return L
    
a = pr(100001)

li = [0]*(100001)
for i in range(1,100000,2):
    if a[i] and a[(i+1)//2]:
        li[i] = 1
        
from itertools import accumulate
b = list(accumulate(li))

for i in range(q):
    l,r = map(int,input().split())
    print(b[r]-b[l-1])