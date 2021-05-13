n=int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][0][0][0]=1
MOD=10**9+7
# 0,1,2,3
# T,A,C,G
# NG
# AGC:132
# GAC:312
# ACG:123
# A?GC:1?32
# AG?C:13?2

for i in range(n):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4): # nxt
                    if b==1 and c==3 and d==2: # AGC
                        continue
                    if b==3 and c==1 and d==2: # GAC
                        continue
                    if b==1 and c==2 and d==3:  # ACG
                        continue
                    if a==1 and c==3 and d==2:  # ACG
                        continue
                    if a==1 and b==3 and d==2:  # ACG
                        continue

                    dp[i+1][b][c][d] += dp[i][a][b][c]
                    dp[i+1][b][c][d]%=MOD
ans=0
for a in range(4):
    for b in range(4):
        for c in range(4):
            ans+=dp[-1][a][b][c]
print(ans%MOD)