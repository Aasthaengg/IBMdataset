import collections
n = int(input())
c = collections.Counter([ input() for i in range(n) ])
ma = max(c.values())
print(*sorted([ i for i, j in c.items() if j == ma ]), sep='\n')