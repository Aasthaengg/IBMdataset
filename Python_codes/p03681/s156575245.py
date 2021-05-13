n,m = map(int,input().split())
mod = 10**9 + 7

if abs(n-m) >= 2:
    print(0)
    exit()

if n == m:
    tmp = 1
    for i in range(1,n+1):
        tmp = (tmp*i)%mod
    ans = (2*tmp*tmp)%mod
else:
    tmp = 1
    for i in range(1,min(n,m)+1):
        tmp = (tmp*i)%mod
    ans = (tmp*tmp*max(n,m))%mod

print(ans)


