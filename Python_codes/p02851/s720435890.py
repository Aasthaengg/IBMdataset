import sys
input = sys.stdin.readline
from collections import *

N, K = map(int, input().split())
A = list(map(int, input().split()))
acc = [0]

for Ai in A:
    acc.append(acc[-1]+Ai)

cnt = defaultdict(int)
ans = 0

for i in range(N+1):
    ans += cnt[(acc[i]-i)%K]
    cnt[(acc[i]-i)%K] += 1
    
    if i>=K-1:
        j = i-(K-1)
        cnt[(acc[j]-j)%K] -= 1

print(ans)