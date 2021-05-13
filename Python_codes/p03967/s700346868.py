import collections
S=list(input())
_S=collections.Counter(S)
count=(_S["g"]-_S["p"])//2
print(count)
