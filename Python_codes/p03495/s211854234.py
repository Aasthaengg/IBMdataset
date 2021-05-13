ma = lambda :map(int,input().split())
n,k = ma()
A = list(ma())
import collections
co = collections.Counter(A)
l = sorted(list(co.values()))

print(sum(l[0:len(l)-k]))
