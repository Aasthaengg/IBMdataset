def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
def V(n):
    if n<=0:return 1
    if n==1:return 2
    if n==2:return 3
    cnt = n+1
    for k in range(2,(n+1)//2+1):
        cnt = (cnt+((A[n-k+1]*B[k])%p*B[n-2*k+1])%p)%p
    return cnt
        
p = 10**9+7
H,W,K = map(int,input().split())
A = [1 for _ in range(W+1)]
for i in range(2,W+1):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(W+1)]
B[W] = pow(A[W],p-2)
for i in range(W-1,1,-1):
    B[i] = ((i+1)*B[i+1])%p
dp = [[0 for _ in range(W+2)] for _ in range(H+1)]
dp[1][1] = V(W-2)
if W>=2:
    dp[1][2] = V(W-3)
for h in range(2,H+1):
    for k in range(1,W+1):
        dp[h][k] = ((dp[h-1][k-1]*V(k-3)*V(W-k-1))%p+(dp[h-1][k]*V(k-2)*V(W-k-1))%p+(dp[h-1][k+1]*V(k-2)*V(W-k-2))%p)%p
print(dp[H][K])