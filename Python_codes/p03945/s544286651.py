from itertools import groupby
S=input()
G=groupby(S)
print(len(list(G))-1)