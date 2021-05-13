# N人の参加者, 参加者iの身長はAi, 背番号の差の絶対値が身長の和に等しい組
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
memo = defaultdict(int)
ans = 0
for i, x in enumerate(A, 1):
    ans += memo[i-A[i-1]]
    memo[i+A[i-1]] += 1
print(ans)
