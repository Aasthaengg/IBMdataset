n = int(input())
A = list(map(int,input().split()))
ans = 0

import collections
c = collections.Counter(A)

A = sorted(set(A))

for i in A:
    a = c[i]
    
    if a > i:
        ans += a-i
        
    elif a < i:
        ans += a
        
print(ans)