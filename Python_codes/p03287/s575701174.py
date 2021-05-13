from itertools import accumulate
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
accum = list(accumulate(A))
count = defaultdict(int)
ans = 0
for i in range(N+1):
    r = accum[i] % M
    ans += count[r]
    count[r] += 1
print(ans)
