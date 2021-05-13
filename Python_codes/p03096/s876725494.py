N = int(input())
K = []
for i in range(N):
  K.append(int(input()))
L = [K[0]]
for j in range(1,N):
  if K[j] != L[len(L)-1]:
    L.append(K[j])
dp = [0]*len(L)
dp[0] = 1
used = [-1]*(max(L)+1)
used[L[0]] = 0
for i in range(1,len(L)):
  if used[L[i]] == -1:
    dp[i] = dp[i-1]
  else:
    dp[i] = (dp[i-1]+dp[used[L[i]]])%(10**9+7)
  used[L[i]] = i
print(dp[len(L)-1])