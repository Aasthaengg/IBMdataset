import itertools

N = int(input())
MOD = 10**9 + 7
ACGT = ["A","C","G","T"]
dp = [ [ [ [0 for l in range(4) ] for k in range(4)] for j in range(4)] for i in range(N+1)]
dp[0][-1][-1][-1] = 1

for i,p,q,r,s in itertools.product(range(N),range(4),range(4),range(4),range(4)):
  if ACGT[q] + ACGT[r] + ACGT[s] not in {'AGC', 'GAC', 'ACG'} \
  and ACGT[p] + ACGT[r] + ACGT[s] != 'AGC' \
  and ACGT[p] + ACGT[q] + ACGT[s] != 'AGC':
    dp[i + 1][q][r][s] += dp[i][p][q][r]
    dp[i + 1][q][r][s] %= MOD   
print(sum(sum(sum(y) for y in x) for x in dp[N]) % MOD)
