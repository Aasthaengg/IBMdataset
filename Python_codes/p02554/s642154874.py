N = int(input())

mod = 10**9+7
def p(a,n):
    ans  = 1
    for i in range (n):
        ans = ans * a % mod
    return ans

print((p(10,N)+p(8,N) - 2* p(9,N))%mod)
