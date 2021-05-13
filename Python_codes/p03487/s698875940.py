# coding: utf-8
import collections
N = int(input())
A=  list(map(int,input().split()))

A.sort()

c = collections.Counter(A)
A_ = list(set(A))
ans = 0
for a in A_:
    #print(c[a],a)
    if a > c[a]:
        ans += c[a]
    else:
        ans += c[a]-a
    
print(ans)