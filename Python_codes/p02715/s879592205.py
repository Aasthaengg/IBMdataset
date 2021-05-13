mod = 10**9+7

def Pow(a, n):
    if n == 0: return 1
    if n%2 == 0:
        return (Pow(a, n//2))**2%mod
    else:
        return Pow(a, n-1)*a%mod

N, K = map(int, input().split())
li = [0] * (K+1)
for i in range(K, 0, -1): 
    li[i] = Pow((K//i), N)
    for j in range(2,K//i+1):
        li[i] = (li[i] - li[i*j])%mod
ans = 0
for i in range(1, K+1):
    ans = (ans + i*li[i])%mod
print(ans)