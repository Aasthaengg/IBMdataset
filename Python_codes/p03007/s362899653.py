import sys
import itertools
import collections
sys.setrecursionlimit(10**7)
def lmi(): return list(map(int, input().split()))

n = int(input())
a = lmi()
a.sort()
b = [-1 for i in range(n)]
b[-1] = 1
for i in range(1, n-1):
    if a[i] > 0:
        b[i] = 1


print(sum([a[i]*b[i] for i in range(n)]))

x = a[0]
for y in [a[i] for i in range(n-1) if b[i] == 1]:
    print(x, y)
    x -= y

y = x
x = a[-1]
print(x, y)
x -= y
for y in [a[i] for i in range(1,n-1) if b[i] == -1]:
    print(x, y)
    x -= y
