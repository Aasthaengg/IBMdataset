import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())

lis = [1 if s=='#' else 0 for s in S]
from itertools import accumulate
lis = list(accumulate(lis))

ans = 10**18
cnt = 0
for i in range(N-1, -1, -1):
    s = S[i]
    ans = min(ans, cnt+lis[i])
    if s=='.':
        cnt += 1
ans = min(ans, cnt)

print(ans)