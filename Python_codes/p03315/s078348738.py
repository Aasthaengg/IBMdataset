import collections
S = list(input())
c = collections.Counter(S)
print(c['+'] - c['-'])