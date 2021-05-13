def solve():
    mod = 10**9+7
    N, K = map(int, input().split())
    lis = [0]*(K+1)
    ans = 0
    for i in range(K,0,-1):
        lis[i] = pow((K//i),N,mod)
        for j in range(2,K//i+1):
            lis[i] -= lis[i*j]
        ans += lis[i]*i
        ans %= mod
    return ans
print(solve())