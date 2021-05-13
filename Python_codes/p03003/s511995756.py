# まずDPを使う理由はあるs[i]=t[j]の時 そのs[i],t[j]を追加した時に増える部分列の場合の数は前の部分列の場合の数+1増えるから
# 前の要素を利用するということはDPを疑う
import sys
input=sys.stdin.readline

mod = 10**9 + 7
n,m = map(int, input().split())
s = input().split()
t = input().split()

dp = [[0] * (m+1) for i in range(n+1)]
S = [[0] * (m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] += (S[i][j] + 1)
            dp[i+1][j+1] %= mod
        else:
            dp[i+1][j+1] = 0 # i番目,j番目を追加すると増える場合の数 iとjが等しくないならば場合の数は増えないから0
        S[i+1][j+1] = S[i][j+1] + S[i+1][j] + dp[i+1][j+1] - S[i][j]
        S[i+1][j+1] %= mod

print(S[n][m]+1)