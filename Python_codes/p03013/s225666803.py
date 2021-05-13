mod = 1000000007
    
N,M = map(int,input().split())

A = [int(input()) for _ in range(M)]

memo = [0]*(100001)

for a in A:
    memo[a] = 1

ruiseki = [0]*(N+1)

ruiseki[0] = 1

for i in range(1,N+1):
    ruiseki[i] = ruiseki[i-1]+ruiseki[i-2]
    if memo[i] != 0:
        ruiseki[i] = 0
print(ruiseki[-1]%mod)