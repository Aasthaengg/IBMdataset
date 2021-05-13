import sys
from collections import defaultdict
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
S = [LI() for _ in range(M)]
P = LI()

ans = 0
for i in range(1 << N):
    d = defaultdict(int)
    for j in range(N):
        if (i >> j) & 1:
            d[j] = 1
    for k in range(M):
        if sum(d[l-1] for l in S[k][1:]) % 2 != P[k]:
            break
    else:
        ans += 1

print(ans)
