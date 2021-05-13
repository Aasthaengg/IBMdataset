m,n = list(map(int, input().split()))
MOD=10**9+7
if abs(m-n) > 1:
    print(0)
    exit()

def fact(x):
    ans=1
    for i in range(2, x+1):
        ans=ans%MOD*i
    return ans

if m>n:
    n,m = m,n
    
f = fact(m)
if m==n:
    print(f * f * 2 % MOD)
else:
    print(f * f * n % MOD)