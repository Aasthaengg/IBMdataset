M = (10**9+7)
s = list(input())[::-1]

mo = []
fixed = 0
for i in range(len(s)):
  if s[i]!='?':
    t = int(s[i])
    fixed += (t*pow(10,i,13))
    fixed %= 13
  else:
    t = []
    for j in range(10):
      t.append((j*pow(10,i,13)%13))
    mo.append(tuple(t))

if len(mo)==0:
  if fixed == 5:
    print(1)
  else:
    print(0)
  exit()
  
dp = [[-1]*13 for _ in range(len(mo))]

for m in mo[0]:
  dp[0][m] = 1
for i in range(len(mo)-1):
  for j in range(13):
    if dp[i][j]==-1:
      continue
    dp_i = dp[i+1]
    dp_j = dp[i]
    for m in mo[i+1]:
      p = (j+m)%13
      if dp_i[p] == -1:
        dp_i[p] = 0
      dp_i[p] += dp_j[j]
      dp_i[p]  %= M

ans = dp[-1][(18-fixed)%13] % M 
if dp[-1][(18-fixed)%13] == -1:
  print(0)
  exit()
print(ans)