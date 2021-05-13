import sys
input = lambda : sys.stdin.readline().rstrip()
mod = 10**9 + 7

s = input()

from collections import Counter

c = Counter(s)

A = c["a"]
B = c["b"]
C = c["c"]

if len(c.keys()) == 1:
    if len(s) > 1:
        print("NO")
    else:
        print("YES")
    sys.exit()

if len(c.keys()) == 2:
    if A + B + C == 2:
        print("YES")
    else:
        print("NO")
    sys.exit()

A -= min(c.values())
B -= min(c.values())
C -= min(c.values())

if A >= 2 or B >= 2 or C >= 2:
    print("NO")
else:
    print("YES")