S=input()
N=len(S)
from collections import Counter
C=Counter(S)
mn=N
mx=0
for c in ['a','b','c']:
    mx=max(mx,C[c])
    mn=min(mn,C[c])
print('YES' if mx-mn<=1 else 'NO')