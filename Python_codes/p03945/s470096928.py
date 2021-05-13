from itertools import groupby

S=input()
G=groupby(S)
g=[len(list(i)) for i,_ in G]
print(sum(g)-1)