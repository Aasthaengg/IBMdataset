from itertools import product

N = int(input())

MOD = 10**9 + 7

# dp[s][i][j][k] = str[s:s+3]が(i,j,k)となる個数の数え上げ
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N-2)]

# 初期条件
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i==0 and j==1 and k==2: continue #AGC
            if i==0 and j==2 and k==1: continue #ACG
            if i==1 and j==0 and k==2: continue #GAC
            dp[0][i][j][k] = 1

# 先頭から末尾に向けてループ
for i in range(N-3):
    # 確定している文字列 (ppp,pp,p)
    for ppp in range(4):
        for pp in range(4):
            for p in range(4):
                # 次の文字 (n)
                for n in range(4):
                    if pp==0 and p==1 and n==2: continue #AGC
                    if pp==0 and p==2 and n==1: continue #ACG
                    if pp==1 and p==0 and n==2: continue #GAC
                    if ppp==0 and p==1 and n==2: continue #A?GC
                    if ppp==0 and pp==1 and n==2: continue #AG?C
                    dp[i+1][pp][p][n] += dp[i][ppp][pp][p]
                    dp[i+1][pp][p][n] %= MOD

ans = sum(sum(sum(a) for a in b) for b in dp[-1])
print(ans % MOD)