from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

s = input()
t = input()[::-1]

if s == t:
    print("YES")
else:
    print("NO")