import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
from math import sqrt

deg = int(sqrt(N*2))

if N*2!=deg*(deg+1):
    print('No')
else:
    print('Yes')
    print(deg+1)
    ans = [[] for _ in range(deg+1)]
    now_len = deg
    cnt = 1
    for d in range(deg+1):
        ans[d].extend(list(range(cnt, cnt+now_len)))
        for i, c in enumerate(range(cnt, cnt+now_len), 1):
            ans[d+i].append(c)
        cnt += now_len
        now_len -= 1
    for i in range(deg+1):
        print(deg, *ans[i])