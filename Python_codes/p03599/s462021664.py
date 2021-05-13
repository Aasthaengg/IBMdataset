A,B,C,D,E,F = map(int,input().split())

dp = [[False]*(F-100*i+1) for i in range(F//100+1)]
dp[0][0] = True
dp[A][0] = True

for i in range(A,F//100+1):
    for j in range(C,F-100*i+1):
        if i < B and j < D:
            if (dp[i-A][j] or dp[i][j-C]) and j<=i*E:
                dp[i][j] = True
        elif i >= B and j < D:
            if (dp[i-A][j] or dp[i-B][j] or dp[i][j-C]) and j<=i*E:
                dp[i][j] = True
        elif i < B and j >= D:
            if (dp[i-A][j] or dp[i][j-C] or dp[i][j-D]) and j<=i*E:
                dp[i][j] = True
        else:
            if (dp[i-A][j] or dp[i-B][j] or dp[i][j-C] or dp[i][j-D]) and j<=i*E:
                dp[i][j] = True

#print(dp)
#print(dp[5])
#print(dp[5][500])

mi = A
mj = 0
for i in range(F//100+1):
    for j in range(F-100*i+1):
        if dp[i][j] and (j*(100*mi+mj) > mj*(100*i+j)):
            mi = i
            mj = j
            #print(mi,mj)
print(100*mi+mj,mj)
