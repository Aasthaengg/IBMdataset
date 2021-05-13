from itertools import groupby


s = input()
g = list(groupby(s))
print(len(g) - 1)