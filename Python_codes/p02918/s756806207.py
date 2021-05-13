import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from math import ceil
N, K = mapint()
S = list(str(input()))

old = S[0]
lis = []
cnt = 1
for i in range(1, N):
    s = S[i]
    if s!=old:
        lis.append(cnt)
        old = s
        cnt = 1
    else:
        cnt += 1
lis.append(cnt)
for l in range(K):
    if len(lis)>=3:
        l1 = lis.pop()
        l2 = lis.pop()
        lis[-1] += (l1+l2)
    elif len(lis)>=2:
        l1 = lis.pop()
        lis[-1] += l1
        break
    else:
        break

ans = sum([i-1 for i in lis])
print(ans)