import itertools
s = list(input())
gr = list(itertools.groupby(s))
print(len(gr)-1)