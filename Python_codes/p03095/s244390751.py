from math import factorial
from collections import Counter
p=10**9+7

N=int(input())
S=input()
T=list(S)
d=dict(Counter(T))

var=1
for num in d:
  var = var*(d[num]+1) %p

print(var-1)
