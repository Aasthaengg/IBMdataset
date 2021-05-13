n, k = map(int, input().split())
if n - 1 < k:
    k = n-1
mod = 10**9+7
cmb1 = [1]*(n+1)
cmb2 = [1]*n
x = [0]*(n+1)
def Pow(a, n):
    if n == 0: return 1
    if n%2 == 0:
        return (Pow(a, n//2))**2%mod
    else:
        return Pow(a, n-1)*a%mod
for i in range(1,n+1):
    x[i] = Pow(i, mod-2)
for i in range(1,n+1):
    cmb1[i] = cmb1[i-1]*(n+1-i)%mod*x[i]%mod
for i in range(1,n):
    cmb2[i] = cmb2[i-1]*(n-i)%mod*x[i]%mod
ans = 0    
for i in range(k+1):
    ans = ((cmb1[i]*cmb2[i])%mod + ans)%mod
print(ans)