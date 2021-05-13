N = int(input())
A = ['A', 'C', 'G', 'T']
dp = [[0]*64 for _ in range(N+1)]
MOD = 10**9+7

for i in range(4):
    for j in range(4):
        for k in range(4):
            if A[i]+A[j]+A[k] in ['AGC', 'ACG', 'GAC']:
                continue

            dp[3][16*k+4*j+i] = 1
    
for i in range(3, N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if A[k]+A[l]+A[m] in ['AGC', 'ACG', 'GAC']:
                        continue
                    
                    if A[j]+A[l]+A[m]=='AGC':
                        continue
                    
                    if A[j]+A[k]+A[m]=='AGC':
                        continue
                    
                    dp[i+1][16*m+4*l+k] += dp[i][16*l+4*k+j]
                    dp[i+1][16*m+4*l+k] %= MOD

print(sum(dp[N])%MOD)