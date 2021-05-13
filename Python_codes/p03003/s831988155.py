import sys,heapq
from collections import deque,defaultdict
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
R = 10**9 + 7
def ddprint(x):
  if DBG:
    print(x)

n,m = inm()
s = inl()
t = inl()
dp = [ [0] * (m+1) for i in range(n) ]
dp[0][0] = 1 if s[0]==t[0] else 0
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + (1 if s[i]==t[0] else 0)
for j in range(1,m):
    dp[0][j] = dp[0][j-1] + (1 if s[0]==t[j] else 0)

sh = defaultdict(list)
for i in range(1,n):
    sh[s[i]].append(i)

for j in range(1,m):
    x = 0
    acc = [0] * (n+1)
    for z in sh[t[j]]:  # s[z]==t[j]
        x = (x+dp[z-1][j-1]+1)%R  # z>0
        acc[z] = x
    for i in range(1,n):
        acc[i] = (acc[i-1] if acc[i]==0 else acc[i])

    for i in range(1,n):
        x = dp[i][j-1]
        #for z in sh[t[j]]:  # s[z]==t[j]
        #  if z<=i:
        #    x = (x+dp[z-1][j-1]+1)%R  # z>0
        x += acc[i]
        if t[j]==s[0]:
            x += 1
        dp[i][j] = x%R

if DBG:
    for i in range(n):
        print(dp[i])
print((dp[n-1][m-1]+1)%R)
