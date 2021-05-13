import collections
s = list(input())
c = collections.Counter(s)
Ng = c["g"]
Np = c["p"]
n = Ng-Np
print(n//2)