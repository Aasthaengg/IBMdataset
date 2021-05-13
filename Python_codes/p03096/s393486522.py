import sys
input = sys.stdin.readline
N = int(input())
c2 = [int(input()) for _ in range(N)]
mod = 10**9+7
#圧縮
c = [c2[0]-1]
n = N
for i in range(1,N):
    if c2[i] == c2[i-1]:
        n -= 1
        continue
    c.append(c2[i]-1)

#used[i]:色iが最後に登場したindex
#初期値:-1
used = [-1]*(max(c)+1)
used[c[0]] = 0
#dp[i]:i番目まででの場合の数
dp = [0]*n
dp[0] = 1
for i in range(1,n):
    if used[c[i]] == -1:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1]+dp[used[c[i]]])%mod
    used[c[i]] = i

print(dp[-1])