def find(N,K):
    MOD = 10**9+7
    number = [1]*(K+1)
    for i in range(K,0,-1):
        number[i] = pow(K//i,N,MOD)
        for j in range(2,K+1):
            if i*j>K:
                break
            number[i] -= number[i*j]
            number[i] %= MOD
    ans = 0
    for k in range(1,K+1):
        ans += number[k]*k
        ans %= MOD
    return ans
N,K = list(map(int,input().strip().split()))
print(find(N,K))