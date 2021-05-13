import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

S = str(input())
N = len(S)

h_all = 0
for i in range(N):
    if S[i]=='?':
        h_all += 1

a = 0
b = 0
h = 0
numAB = 0
numAH = 0
numHB = 0
numHH = 0
dp = [0]*N

beki3 = pow(3,h_all-3,mod) if h_all>=4 else 1
beki2 = beki3*3 % mod if h_all>=3 else 1
beki1 = beki2*3 %mod if h_all>=2 else 1
beki0 = beki1*3 %mod if h_all>=1 else 1

for i in range(N):
    if S[i]=='A':
        if i>=1:
            dp[i] = dp[i-1]
        a += 1
    elif S[i]=='B':
        if i>=1:
            dp[i] = dp[i-1]
        numAB += a
        numHB += h
        b += 1
    elif S[i]=='?':
        if i>=1:
            if h_all>=1:
                dp[i] = (dp[i-1]+numAB*beki1) %mod
            if h_all>=2:
                dp[i] = (dp[i]+numAH*beki2) %mod
                dp[i] = (dp[i]+numHB*beki2) %mod
            if h_all>=3:
                dp[i] = (dp[i]+numHH*beki3)%mod
        numAH += a
        numHH += h
        h += 1
    else:
        if i>=1:
            dp[i] = (dp[i-1]+numAB*beki0) %mod
            if h_all>=1:
                dp[i] = (dp[i]+numAH*beki1) %mod
                dp[i] = (dp[i]+numHB*beki1) %mod
            if h_all>=2:
                dp[i] = (dp[i]+numHH*beki2)%mod

print(dp[N-1])