import sys
readline = sys.stdin.readline

N = int(readline())
X = readline().rstrip()

X0 = int(X, 2)
count1 = X.count("1")

X0mod0to1 = X0 % (count1 + 1) # 0->1に変化した際の、X0を割った余り
if count1 > 1:
  X0mod1to0 = X0 % (count1 - 1) # 1->0に変化した際の、X0を割った余り
else:
  X0mod1to0 = 0

from collections import defaultdict
dp = defaultdict(int)
dp[0] = 0
def f(x): # 愚直にf(x)を求める式
  if x in dp:
    return dp[x]
  pc = bin(x).count("1")
  val = f(x % pc) + 1
  dp[x] = val
  return val
  
val0to1 = 1
val1to0 = 1
ans = [-1] * N

for i in range(N - 1, -1, -1): # 下の桁から順に、f(Xi)の値を求める
  if X[i] == "0": # 0を1に変える場合
    pat = (X0mod0to1 + val0to1 % (count1 + 1)) % (count1 + 1)
    ans[i] = f(pat) + 1
  elif X[i] == "1": # 1を0に変える場合
    if count1 > 1:
      pat = (X0mod1to0 - val1to0 % (count1 - 1)) % (count1 - 1)
      ans[i] = f(pat) + 1
    else:
      ans[i] = 0
  val0to1 = val0to1 * 2 % (count1 + 1)
  if count1 != 1:
    val1to0 = val1to0 * 2 % (count1 - 1)

print(*ans, sep = "\n")