import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
from collections import defaultdict
dic1 = defaultdict(int)
for i in range(3):
    n,m = map(int,readline().split())
    dic1[n] += 1
    dic1[m] += 1

lst1 = list(dic1.values())
lst1.sort()

if lst1 == [1,1,2,2]:
    print("YES")
else:
    print("NO")