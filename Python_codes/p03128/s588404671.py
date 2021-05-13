N,M = map(int,input().split())
List = list(map(int,input().split()))

a = [0,2,5,5,4,5,6,3,7,6]

kazu = [a[List[i]] for i in range(M)]

def dddd(kazu,X):
  dp = [ [ -float('inf') for j in range(X+1)]  for i in range(M)]
  for i in range(M):
    dp[i][0] = 0

  for i in range(M):
    for j in range(X+1):
      if kazu[i] <= j:
        dp[i][j] = max(dp[i][j-kazu[i]] + 1,dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  return dp[-1]
   
keta_arr = dddd(kazu,N)
keta = keta_arr[-1]
List.sort(reverse=True)
ans = []

while keta>0:
  for aa in List:
    k = a[aa]
    if N-k < 0:
      continue
    if N-k >= 0:
      if keta_arr[N-k] == keta-1:       
        ans.append(aa)
        N = N-k
        keta -= 1
        break
ans.sort(reverse=True)
print(int(''.join(map(str,ans))))