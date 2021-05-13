import collections
 
S = list(input())
c = collections.Counter(S)
 
if max([c['a'], c['b'], c['c']]) - min([c['a'], c['b'], c['c']]) <= 1:
    print('YES')
else:
    print('NO')