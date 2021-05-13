import collections
s = list(input())
c = collections.Counter(s)
print(min(c["0"], c["1"])*2)