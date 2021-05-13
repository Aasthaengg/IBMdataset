import itertools

N = int(input())
MOD = 10**9 + 7

base = ['A', 'C', 'G', 'T']
base3 = list(itertools.product(base, repeat=3))
index_dict = dict(zip(base3, range(64)))


def is_NG(b, s):
  for i in range(4):
    lb = list(b) + [s]
    if i >= 1:
      lb[i-1], lb[i] = lb[i], lb[i-1]
    if ''.join(lb).count('AGC') == 1:
      return True
  return False


# 0:A->A->A, 1:A->A->C, 2:A->A->G, 3:A->A->T, ...
dp = [[0]*64 for i in range(N)]
dp[2] = [1] * 64
for b in [('A', 'G', 'C'), ('A', 'C', 'G'), ('G', 'A', 'C')]:
  dp[2][index_dict[b]] = 0


for i in range(3, N):
  for j in range(64):
    b = base3[j]
    if is_NG(b, 'C'):
      for s in 'AGT':
        idx = index_dict[(b[1], b[2], s)]
        dp[i][idx] += dp[i-1][j]
        dp[i][idx] %= MOD
    elif is_NG(b, 'G'):
      for s in 'ACT':
        idx = index_dict[('A', 'C', s)]
        dp[i][idx] += dp[i-1][j]
    else:
      for s in 'ACGT':
        idx = index_dict[(b[1], b[2], s)]
        dp[i][idx] += dp[i-1][j]
        dp[i][idx] %= MOD
        

ans = sum(dp[-1]) % MOD
print(ans)