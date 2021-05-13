import sys
input = sys.stdin.readline
from collections import *

N, M = map(int, input().split())
ins = [0]*N
outs = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    ins[y-1] += 1
    outs[x-1].append(y-1)

q = deque([v for v in range(N) if ins[v]==0])
dp = [0]*N

while q:
    v = q.popleft()
    
    for nv in outs[v]:
        dp[nv] = max(dp[nv], dp[v]+1)
        ins[nv] -= 1
        
        if ins[nv]==0:
            q.append(nv)

print(max(dp))