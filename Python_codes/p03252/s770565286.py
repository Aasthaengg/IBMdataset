import sys
import collections
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

scl = sorted(list(collections.Counter(s).values()))
tcl = sorted(list(collections.Counter(t).values()))

if scl == tcl:
    print('Yes')

else:
    print('No')
