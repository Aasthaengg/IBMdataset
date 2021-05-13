N,K = map(int,input().split())
MOD = 10**9+7
res = 0
curmin,curmax = 0, N
mini,maxi = 1, N-1
for i in range(1,N+2):
  if i == N+1:
    # print(1)
    res += 1
  else:
    if i >= K:
      # print(curmin,curmax)
      res = (res + curmax - curmin + 1) % MOD
    curmin += mini
    curmax += maxi
    mini += 1
    maxi -= 1

print(res % MOD)
