'''
in
-----
7
2
9
4
5
1
6
10
'''
'''
out
-----
8
'''
from collections import defaultdict
dp = defaultdict(lambda:int(0))

N = int(input())
L = [0] * (N +2)
for i in range(0, N):
    L[i] = list(map(int, input().split()))

for i in range(0, N):
    for j in range(0, 3):
        for k in range(0, 3):
            if j == k:
                continue
            dp[(i+1,k)] = max(dp[i+1,k], dp[(i,j)] + L[i][k])

print(max(dp.values()))
