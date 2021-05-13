L=[1]
n=int(input())
x = 6
y = 9
while x <= n:
  L.append(x)
  x *= 6
while y <= n:
  L.append(y)
  y *= 9
L.sort()#[1,6,9,36,81]
dp = [float("Inf")]*(n+1)
dp[0] = 0
for i in range(n+1):#0~81
  for j in L:#1,6,9
    if i+j <= n:
      dp[i+j] = min(dp[i+j],dp[i]+1)#dp=[0,1,...1,.1]
    else:
      break
print(dp[n])