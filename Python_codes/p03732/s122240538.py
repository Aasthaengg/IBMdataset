import sys
input = sys.stdin.readline

N,W=map(int,input().split())
S=[list(map(int,input().split())) for i in range(N)]

from collections import defaultdict
DP = defaultdict(int)
DP[0]=0

for w,v in S:
    for w2 in sorted(DP.keys(),reverse=True):
        if w+w2<=W:
            DP[w+w2]=max(DP[w+w2],DP[w2]+v)

print(max(DP.values()))