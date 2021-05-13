from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

from collections import Counter

s = input()
C = Counter(s)

a = C["a"]
b = C["b"]
c = C["c"]

li = [a,b,c]
li.sort()

if li[0]+1 >= li[2]:
    print("YES")
else:
    print("NO")