N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

unused = [3] * N
ans = 1
for i in range(N):
    if A[i] == 0:
        ans *= unused[0]
        unused[0] -= 1
    else:
        ans *= unused[A[i]] - unused[A[i]-1]
        unused[A[i]] -= 1
    ans %= mod
        
print(ans % mod)
