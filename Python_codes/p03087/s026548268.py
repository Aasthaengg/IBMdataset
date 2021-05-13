import re
import itertools

N,Q = list(map(int, input().split()))
s = input()

pos = [m.end() for m in re.finditer(r'AC', s)]

dp = [0] * (N+1)
for p in pos:
    dp[p] = 1
dp = list(itertools.accumulate(dp))

ans=[]    
for _ in range(Q):
    l,r = list(map(int, input().split()))
    ans.append(dp[r]-dp[l])

print(*ans, sep='\n')