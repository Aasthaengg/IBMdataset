import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
n = len(s)
m = len(t)

from collections import deque

dic = {}
for i in range(ord("a"), ord("z") + 1):
    dic[chr(i)] = deque([])


for i in range(n):
    dic[s[i]].append(i + 1)

cnt = 0
res = 0
from bisect import bisect

for i in t:
    if len(dic[i]) == 0:
        print(-1)
        sys.exit()
    idx = bisect(dic[i], cnt)
    if idx >= len(dic[i]):
        res += 1
        cnt = dic[i][0]
    else:
        cnt = dic[i][idx]

print(n * res + cnt)
