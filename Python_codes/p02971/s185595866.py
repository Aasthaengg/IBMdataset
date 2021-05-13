# C - Exception Handling 
# 累積 max の問題
N = int(input())
A = [int(input()) for _ in range(N)]

# lm[i]; iより左にある値の中の最大値。 便宜上 lm[0] = 0 (i = 0 より左はない)
lm = [0]*N
# rm[i]; iより右にある値の中の最大値。 便宜上 lr[n-1] = 0 (i = n-1 より右はない)
rm = [0]*N
# 求める値は max(lm[i], rm[i]) (i = 0,1,2,...,n-1) 

# i = 0 より右にある値は i = 1,2,...,n-1 の n-1 個
for l in range(1,N): 
    lm[l] = max(lm[l-1], A[l-1])
    
# i = N-1 より左にある値は i = 0,1,2,...,n-2 の n-1 個
for r in  range(N-2,0-1,-1):# range(a,b) は [a,b)であることに注意
    rm[r] = max(rm[r+1],A[r+1])


for a in range(N):
    ans = max(lm[a],rm[a])
    print(ans)