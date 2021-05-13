import collections
import sys
readline = sys.stdin.readline

n = int(input())
d = collections.Counter([int(x) for x in readline().rstrip().split()])
m = int(input())
t = collections.Counter([int(x) for x in readline().rstrip().split()])
for i in t.items():
    if i[1] > d[i[0]]:
        print("NO")
        exit()
print("YES")
