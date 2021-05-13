import collections
S = input()
col_S = collections.Counter(S) 
print(min(col_S['0'],col_S['1'])*2)
