N, MOD = int(input()), 10**9+7
memo = [{} for _ in range(N+1)]

def DFS(i, w):
    if w in memo[i]:
        return memo[i][w]
    if i == N:
        return 1
    
    ans = 0
    for c in 'ACGT':
        if w + c not in NG:
            ans = (ans + DFS(i+1, w[1:] + c)) % MOD
    memo[i][w] = ans
    return ans

if N == 3:
    print(61)
else:
    ans, NG = 0, set(['AGGC', 'ATGC', 'AGTC'])
    for w in ['AGC', 'GAC', 'ACG']:
        for c in 'ACGT':
            NG.add(c+w)
            NG.add(w+c)
    for w in [x+y+z for x in 'ACGT' for y in 'ACGT' for z in 'ACGT' if x+y+z not in ['AGC', 'GAC', 'ACG']]:
        ans = (ans + DFS(3, w)) % MOD
    print(ans)