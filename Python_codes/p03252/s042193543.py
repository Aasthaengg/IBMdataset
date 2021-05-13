import sys
import collections

s = list(map(str,input()))
t = list(map(str,input()))
cnts = collections.Counter(s)
cntt = collections.Counter(t)
cs = sorted(cnts.values())
ct = sorted(cntt.values())

if len(s) != len(t):
    print("No")
    sys.exit()

for i,j in zip(cs,ct):
    if i != j:
        print("No")
        sys.exit()

print("Yes")