import sys
input = sys.stdin.readline
s = input()[: -1]
t = s.split("T")
x, y = map(int, input().split())
x -= t[0].count("F")
xm = t[: : 2]
ym = t[1: : 2]
xl = 0
yl = 0
if "F" in t[0]: xm = xm[1: ]
for i in range(len(xm)): xl += len(xm[i])
for i in range(len(ym)): yl += len(ym[i])
if xl < abs(x) or (yl < abs(y)):
  print("No")
  exit(0)
#print(xm, ym)
dp = [[0] * (xl * 2 + 1) for _ in range(len(xm) + 1)]
dp[0][xl] = 1
for i in range(len(xm)):
  for j in range(xl * 2 + 1):
    z = len(xm[i])
    if (j + z) in range(xl * 2 + 1):
      dp[i + 1][j + z] |= dp[i][j]
    if (j - z) in range(xl * 2 + 1):
      dp[i + 1][j - z] |= dp[i][j]
if dp[-1][xl + x] == 0:
  print("No")
  exit(0)
dp = [[0] * (yl * 2 + 1) for _ in range(len(ym) + 1)]
dp[0][yl] = 1
for i in range(len(ym)):
  for j in range(yl * 2 + 1):
    z = len(ym[i])
    if (j + z) in range(yl * 2 + 1):
      dp[i + 1][j + z] |= dp[i][j]
    if (j - z) in range(yl * 2 + 1):
      dp[i + 1][j - z] |= dp[i][j]
if dp[-1][yl + y] == 0:
  print("No")
  exit(0)
print("Yes")