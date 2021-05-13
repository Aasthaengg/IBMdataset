import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


A = LS2()
N = len(A)

# 答えは、(Ai != Aj たる 1 <= i < j <= N の個数) +1

from collections import defaultdict

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for key in d.keys():
    ans += d[key]*(N-d[key])

ans //= 2
ans += 1
print(ans)
