N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
MOD = 1000000007
memo = [0]*(N+1)
memo[0] = 1
if 1 not in A:
    memo[1] = 1
for i in range(2, N+1):
    if i not in A:
        memo[i] = (memo[i-2] + memo[i-1])%MOD
print(memo[N])
