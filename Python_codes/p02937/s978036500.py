from bisect import *
from collections import defaultdict
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
L = len(S)

dic = defaultdict(list)
for i, s in enumerate(S):
    dic[s].append(i)


s0 = -1
cnt = 0
for t in T:
    if not dic[t]:
        print(-1)
        exit()
    p = bisect_right(dic[t],s0)
    if p >= len(dic[t]):
        cnt += 1
        s0 = min(dic[t])
    else:
        s0 = dic[t][p]

print(L*cnt+s0 +1)