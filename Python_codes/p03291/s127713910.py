MOD = 10**9 + 7
S = input()
N = len(S)
target = 'ABC'
n = len(target)
cur = [0]*(n+1)
cur[0] = 1
for s in S:
    for w in range(n):
        if s == target[w]:
            cur[w+1] += cur[w]
            cur[w+1] %= MOD
            break
    else: # case of '?'
        for w in range(n-1,-1,-1):
            cur[w+1] = (cur[w+1]*3 + cur[w]) % MOD
        cur[0] *= 3
        cur[0] %= MOD
print(cur[-1])