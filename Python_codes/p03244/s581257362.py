import sys
input = sys.stdin.readline
from collections import *

n = int(input())
v = list(map(int, input().split()))
cnt1 = Counter([v[i] for i in range(n) if i%2==0])
cnt2 = Counter([v[i] for i in range(n) if i%2==1])
cnt1[-1] = 0
cnt2[-1] = 0
k1 = [k for k in cnt1.keys()]
k1.sort(key=lambda x: cnt1[x], reverse=True)
k2 = [k for k in cnt2.keys()]
k2.sort(key=lambda x: cnt2[x], reverse=True)

if k1[0]!=k2[0]:
    print(n-cnt1[k1[0]]-cnt2[k2[0]])
else:
    print(min(n-cnt1[k1[0]]-cnt2[k2[1]], n-cnt1[k1[1]]-cnt2[k2[0]]))