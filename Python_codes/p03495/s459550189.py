n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

import collections
c = collections.Counter(A)
c = c.most_common()

m = len(set(A))

if m > k:
    for i in range(m-k):
        ans += c[-1-i][1]
        
print(ans)