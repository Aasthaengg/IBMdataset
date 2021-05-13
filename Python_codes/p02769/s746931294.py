n,k = map(int,input().split())
m = min(k,n-1)
mod = 10**9+7

A = [0]*(m+1)
B = [0]*(m+1)

for i in range(m+1):
    if i == 0:
        A[0] = 1
        B[0] = 1
    else:
        A[i] = ((A[i-1]*(n-i+1))*pow(i,mod-2,mod)) % mod
        B[i] = ((B[i-1]*(n-i))*pow(i,mod-2,mod)) % mod

ans = 0
for i in range(m+1):
    ans = (ans+A[i]*B[i]) % mod

print(ans % mod)