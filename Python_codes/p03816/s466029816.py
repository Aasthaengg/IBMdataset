N = int(input())
A = list(map(int,input().split()))
from collections import Counter
L = dict(Counter(A))
val = list(L.values())
Nval = len(val)
X = sum(val)-Nval
if X%2==0:
    print(Nval)
else:
    print(Nval-1)
