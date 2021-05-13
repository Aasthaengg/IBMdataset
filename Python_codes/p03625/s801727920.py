n = int(input())
A = list(map(int,input().split()))
ans = 0

import collections
c = collections.Counter(A)

two = []
four = []

for i in sorted(set(A)):
    a = c[i]
    
    if a > 1:
        two.append(i)
        
    if a > 3:
        four.append(i)
        
if len(two) > 0:
    two = sorted(two)
    ans = two[-1] * two[-2]
    
if len(four) > 0:
    ans = max(max(four)**2,ans)
    
print(ans)