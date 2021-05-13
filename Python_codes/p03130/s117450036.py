a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())

A=[a1,b1,a2,b2,a3,b3]

import collections
L=collections.Counter(A)

if set(list(L.values()))==set([1,2,2,1]):
    print('YES')
else:
    print('NO')