N, K, S = map(int, input().split())
mod = 10**9
rlt = [S]*K+[(S+1)%mod]*(N-K)

print(" ".join(map(str, rlt)))