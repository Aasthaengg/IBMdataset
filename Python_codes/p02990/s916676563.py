def solve():
    mod = 10**9+7
    N, K = map(int, input().split())
    ans = []
    combs1 = [1]*K
    combs2 = [1]*(K+1)
    for i in range(1,K):
        combs1[i] = combs1[i-1]*(K-i)*pow(i,mod-2,mod)%mod
    for i in range(1,K+1):
        combs2[i] = combs2[i-1]*(N-K+2-i)*pow(i,mod-2,mod)%mod
    for i in range(1,K+1):
        ans.append(combs1[i-1]*combs2[i]%mod)
    return ans
print(*solve(),sep='\n')