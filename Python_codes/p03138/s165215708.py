N,K = map(int,input().split())
A = list(map(int,input().split()))


#%%
L = 50
# bins[i]: 2進数でi桁目にある1の数の合計
bins = [0]*L
kb = [0]*L


for i in range(L):    
    for j in range(N):
        bins[i] += A[j]%2
        A[j] >>= 1
    kb[i] = K%2
    K >>= 1

bins.reverse()
kb.reverse()
#%%
start = L

for i,k in enumerate(kb):
    if k==1:
        start = i
        break


#dp[i+1][t]:上からi桁目まで決めたときの最大スコア
#t=0: K未満となるとき，　t=1: Kとその桁まで一致するとき　　
        
dp = [[0]*2 for _ in range(L+1)]



cur = 0
base = 2**(L-1)
for i in range(L):
    if i<start:
        dp[i+1][1] = dp[i][1] + bins[i]*base
        
    elif i==start:
        dp[i+1][0] = dp[i][1]+(bins[i])*base
        dp[i+1][1] = dp[i][1] + (N-bins[i])*base
        
    else:
        if kb[i]:
            dp[i+1][0] = max(dp[i][0] + max(bins[i],N-bins[i])*base,
                             dp[i][1] + (bins[i]) * base)
            
            dp[i+1][1] = dp[i][1] + (N-bins[i])*base      
        else:
            dp[i+1][0] = dp[i][0] + max(bins[i],N-bins[i])*base
            
            dp[i+1][1] = dp[i][1] + (bins[i])*base            
    base >>= 1
        
print(max(dp[L][0],dp[L][1]))

    




