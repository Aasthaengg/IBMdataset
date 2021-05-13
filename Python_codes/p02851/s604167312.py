from itertools import accumulate 
n,k=map(int,input().split())
A=[int(i) for i in input().split()]
S=list(accumulate(A))
S.insert(0,0)

L=[ (s-i)%k  for i,s in enumerate(S)]
def f(l):
    return sum([x*(x-1)//2 for x in l])

from collections import Counter

ans=0
d = Counter(L[1:k])
for i in range(n):
    ans += d[L[i]]
    #print(L[i+1:i+k],d)
    d[L[i+1]] -= 1
    if i+k <= n:
        d[L[i+k]] += 1
print(ans)