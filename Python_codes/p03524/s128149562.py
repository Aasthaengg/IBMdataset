import collections
A = input()
Ac = collections.Counter(A)
maxA = max(Ac.values())
print('YES' if maxA<=(len(A)+2)/3 else 'NO') 
