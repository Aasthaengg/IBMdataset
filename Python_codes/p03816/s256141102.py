n=int(input())
a=list(map(int,input().split()))

import collections
c=collections.Counter(a)
C=c.most_common()

even=0
for i in range(len(C)):
    p,q=C[i]
    if q%2==0:
        even += 1
if even%2==0:
    print(len(C))
else:
    print(len(C)-1)