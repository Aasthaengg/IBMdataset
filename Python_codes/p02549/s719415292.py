N,K = map(int, input().split())
LRs = []
P = 998244353
for _ in range(K):
  l,r = map(int, input().split())
  LRs.append((l,r))
  
memo = [0]*(N+2)
memo[1] = 1
memo[2] = -1
rlt = [0]*(N+2)
rlt[1] = 1


for i in range(1,N+1):
  for t in LRs:
    l = min(t[0]+i,N+1)
    r = min(t[1]+i+1,N+1)
    memo[l] = memo[l]+rlt[i]
    memo[r] = memo[r]-rlt[i]
  rlt[i+1] = (rlt[i]+memo[i+1])%P
  
print(rlt[N])