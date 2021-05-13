n,k = map(int,input().split())
ans = 0
mod = 10**9+7
for i in range(k,n+2):
    M = n*(n+1)//2-(n-i)*(n-i+1)//2
    m = (i-1)*(i)//2
    ans += M-m+1
    ans %= mod
print(ans)