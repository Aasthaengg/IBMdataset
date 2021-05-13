import sys
from collections import Counter
n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))

dc = Counter(d)
tc = Counter(t)

for i in tc.keys():
    if dc[i]<tc[i]:
        print('NO')
        sys.exit()
print('YES')