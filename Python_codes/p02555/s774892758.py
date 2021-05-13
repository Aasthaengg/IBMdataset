import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

m = 10**9 + 7
s = int(input())
if s <= 2:
    print(0)
else:
    dp = [0 for _ in xrange(s+1)]
    for i in xrange(3,s+1):
        dp[i] = 1
        for j in xrange(3,i+1):
            dp[i] += dp[i-j]
            if dp[i] >= m:
                dp[i] = dp[i] % m 
    print(dp[s] %m)
