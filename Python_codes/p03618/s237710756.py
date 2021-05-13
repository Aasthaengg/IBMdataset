import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a = input()
n = len(a)
from collections import defaultdict
d = defaultdict(int)
s = 0
ans = 0
for i,c in enumerate(a):
    ans += (s - d[c])
    d[c] += 1
    s += 1
print(ans+1)