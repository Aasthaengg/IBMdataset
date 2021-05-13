from collections import defaultdict
from itertools import accumulate
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A_acc = [0]+list(accumulate(A))


ans = 0
D = defaultdict(int)
for l in range(N+1):
    t = (A_acc[l]-l) % K
    if l>=K:
      r = (A_acc[l-K]-(l-K))
      D[r%K]-=1
    ans += D[t]
    D[t] += 1


print(ans)
