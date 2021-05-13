N = int(input())

memo = {}

def luca(N):
    if N in memo:
        return memo[N]
    else:
        memo[N] = 0
    if N == 0:
        memo[N] = 2
        return 2
    if N == 1:
        memo[N] = 1
        return 1
    memo[N] = luca(N-1) + luca(N-2)
    return memo[N]

print(luca(N))