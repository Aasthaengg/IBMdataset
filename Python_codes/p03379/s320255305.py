import sys
input = sys.stdin.readline
from collections import *

N = int(input())
X = list(map(int, input().split()))
l = [(i, X[i]) for i in range(N)]
l.sort(key=lambda t: t[1])
ans = [-1]*N

for i in range(N):
    if i<N//2:
        ans[l[i][0]] = l[N//2][1]
    else:
        ans[l[i][0]] = l[N//2-1][1]

for ans_i in ans:
    print(ans_i)