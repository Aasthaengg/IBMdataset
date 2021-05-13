N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

combs = [0]*N
combs[K-1]=1
for i in range(K,N):
    combs[i] = combs[i-1]*i%mod
    combs[i] *= pow(i+1-K,mod-2,mod)
    combs[i] %= mod

def solve(A):
    A.sort()
    ans = 0
    for i in range(N):
        ans += (combs[i]-combs[N-i-1])*A[i]
        ans %= mod
    return ans
print(solve(A))