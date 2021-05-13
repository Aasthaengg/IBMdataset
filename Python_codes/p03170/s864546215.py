import sys
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
N,K = LI()
a = LI()
dp = [0 for _ in range(K+1)]

for i in range(K,-1,-1):
    if dp[i]: continue
    for x in a:
        if i-x >= 0: dp[i-x] = 1
if dp[0] == 1:
    print('First')
else:
    print('Second')