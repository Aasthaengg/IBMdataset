import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, Q = mapint()
S = list(str(input()))
from itertools import accumulate
lis = [0]*N
for i in range(1, N):
    if S[i-1]=='A' and S[i]=='C':
        lis[i] += 1
cum = list(accumulate(lis))

for _ in range(Q):
    l, r = mapint()
    print(cum[r-1]-cum[l-1])