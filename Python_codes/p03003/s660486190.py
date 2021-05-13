"""
愚直に全探索すると、O(2**N+2**M)かかる
制約的にはDPっぽいかな。
あ、これ部分文字列DPの発想に近いな。
dp[i][j] => Sのインデックスi、Tのインデックスjまでみる。インデックスi、インデックスjは使う。
nt[i][j] => Tのi項以降で数字jが出てくるインデックス。
"""
N,M = map(int,input().split())

N += 1
M += 1

S = list(map(int,input().split()))
S = [0]+S
T = list(map(int,input().split()))
T = [0]+T

dp = [[0]*M for _ in range(N)]
mod = 10**9 +7
for j in range(M):
    dp[0][j] = 1

for i in range(1,N):
    for j in range(M):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            if S[i] == T[j]:
                dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[-1][-1])