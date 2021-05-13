import itertools

N = int(input())
MOD = 10**9 + 7

base = ['A', 'C', 'G', 'T']
base3 = list(itertools.product(base, repeat=3))
index_dict = dict(zip(base3, range(64)))

s0 = set((('A', 'G', 'C'), ('A', 'C', 'G'), ('G', 'A', 'C')))
s1 = set((('A', 'A', 'G'), ('C', 'A', 'G'), ('G', 'A', 'G'), ('T', 'A', 'G')))
s2 = set((('A', 'A', 'G'), ('A', 'C', 'G'), ('A', 'G', 'G'), ('A', 'T', 'G')))
s3 = set((('A', 'G', 'A'), ('C', 'G', 'A'), ('G', 'G', 'A'), ('T', 'G', 'A')))
s4 = set((('A', 'G', 'A'), ('A', 'G', 'C'), ('A', 'G', 'G'), ('A', 'G', 'T')))
s5 = set((('A', 'A', 'C'), ('C', 'A', 'C'), ('G', 'A', 'C'), ('T', 'A', 'C')))

# 0:A->A->A, 1:A->A->C, 2:A->A->G, 3:A->A->T, ...
dp = [[0]*64 for i in range(N)]

for j in range(64):
  if base3[j] in s0:
    continue
  
  dp[2][j] = 1


for i in range(3, N):
  for j in range(64):
    b = base3[j]
    idx_b = index_dict[b]
    if b in s1 or b in s2 or b in s3 or b in s4:
      for s in ['A', 'G', 'T']:
        idx = index_dict[(b[1], b[2], s)]
        dp[i][idx] += dp[i-1][idx_b]
        dp[i][idx] %= MOD
    elif b in s5:
      for s in ['A', 'C', 'T']:
        idx = index_dict[('A', 'C', s)]
        dp[i][idx] += dp[i-1][idx_b]
    else:
      for s in ['A', 'C', 'G', 'T']:
        idx = index_dict[(b[1], b[2], s)]
        dp[i][idx] += dp[i-1][index_dict[b]]
        dp[i][idx] %= MOD
        

ans = sum(dp[-1]) % MOD
print(ans)