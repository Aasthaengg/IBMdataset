N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

def mex(L):
  L.sort()
  ans = 0
  for i in L:
    if i <= ans:
      ans += 1
    else:
      break
  return ans

DP = [0] * (K + 1)
M = 100000

for i in range(a[0], K + 1):
  L = []
  for j in range(N):
    if i - a[j] < 0:
      break
    L.append(DP[i - a[j]])
  DP[i] = mex(L)

if DP[-1] == 0:
  print("Second")
else:
  print("First")
