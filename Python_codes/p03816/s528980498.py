import sys;input = lambda : sys.stdin.readline()
import collections
n = int(input())
a = sorted(list(map(int, input().split())))
d = collections.Counter(a)
need = {}
for k,v in d.items():
    if v>1:
        need[k]=v
if (sum(list(need.values()))-len(need))%2==0:
    print(len(set(a)))
else:
    print(len(set(a))-1)
