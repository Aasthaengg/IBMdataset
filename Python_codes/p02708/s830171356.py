n,k = map(int,input().split())
mod = 10**9 + 7
ans = 0
for i in range(k, n+2):
    ans += max(0, n*(n+1)//2 - (n-i)*(n+1-i)//2 - i*(i-1)//2 + 1)
    ans %= mod
print(ans)