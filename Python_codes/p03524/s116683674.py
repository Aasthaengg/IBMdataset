from collections import Counter

lst = list(input())

c = Counter(lst)

A = c['a']
B = c['b']
C = c['c']

if max(max(A, B), C) - min(min(A, B), C) <= 1:
    print ('YES')
else:
    print ('NO')