import itertools
S = input()
G = itertools.groupby(S)
print(len(list(G))-1)