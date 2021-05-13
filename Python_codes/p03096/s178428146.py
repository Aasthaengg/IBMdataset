mod=10**9+7
n=int(input())
arr=[int(input()) for _ in range(n)]
tmp=[arr[0]]
for i in range(1,n):
  if arr[i]!=tmp[-1]:
    tmp.append(arr[i])
n=len(tmp)
arr=tmp
dp=[0]*n
dp[0]=1
g=[[] for _ in range(max(arr)+1)]
for i in range(n):
  g[arr[i]].append(i)
cnt=[0]*(max(arr)+1)
lim=[0]*(max(arr)+1)
for i in range(max(arr)+1):
  lim[i]=len(g[i])
for i in range(n-1):
  dp[i+1]+=dp[i]
  dp[i+1]%=mod
  if cnt[arr[i]]+1<lim[arr[i]]:
    dp[g[arr[i]][cnt[arr[i]]+1]]+=dp[i]
    dp[g[arr[i]][cnt[arr[i]]+1]]%=mod
    cnt[arr[i]]+=1
print(dp[-1]%mod)