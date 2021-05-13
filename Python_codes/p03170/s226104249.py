from sys import stdin
from collections import deque
n,k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
dp = [0]*(k+1)
for i in range(a[0],k+1):
    for j in a:
        if i-j >= 0 and dp[i-j] == 0:
            dp[i] = 1
            break
if dp[-1]%2:
    print('First')
else:
    print('Second')
