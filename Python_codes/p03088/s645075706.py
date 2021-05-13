mod = 10**9+7
n = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][0][0][0] = 1
# 0 -> T
# 1 -> C
# 2 -> G
# 3 -> A

def chk(s):
# NG Case : AG*C A*GC *ACG *GAC *AGC
  if   s[0] == 3 and s[1] == 2 and s[3] == 1: return False
  elif s[0] == 3 and s[2] == 2 and s[3] == 1: return False
  elif s[1] == 3 and s[2] == 1 and s[3] == 2: return False
  elif s[1] == 2 and s[2] == 3 and s[3] == 1: return False
  elif s[1] == 3 and s[2] == 2 and s[3] == 1: return False
  else: return True

def dfs(c, j, k, l):
  for m in range(4):
    if chk([j, k, l, m]):
      dp[c][k][l][m] += dp[c-1][j][k][l]

for i in range(1, n+1):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        dfs(i, j, k, l)

ans = 0
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans += dp[n][i][j][k]
print(ans % mod)