
N, M = map(int, input().split())
A = list(map(int, input().split()))
numbers = [0,2,5,5,4,5,6,3,7,6]


dp = ["-" for i in range(11000)]
dp[0] = ""

def cal(x, y):
  lenx = len(x)
  leny = len(y)
  
  if lenx > leny:
    return x
  if leny > lenx:
    return y
  
  return max(x, y)

for i in range(N):
  if dp[i] == "-": 
    continue

  for j in range(M):
    num = numbers[A[j]]
    dp[i+num] = cal(dp[i] + str(A[j]), dp[i+num])

print(dp[N])