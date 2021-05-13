n=int(input())
lst=list(map(int,input().split()))
if len(set(lst))==1:
    print(n//2)
    exit()
a=sorted(lst[::2])
b=sorted(lst[1::2])

import collections
a=collections.Counter(a)
b=collections.Counter(b)
a=a.most_common()
b=b.most_common()
if a[0][0]!=b[0][0]:
    print(n//2-a[0][1]+n//2-b[0][1])
else:
    print(min(n//2-a[0][1]+n//2-b[1][1],n//2-a[1][1]+n//2-b[0][1]))