N, K = map(int, input().split())
L = []
for _ in range(K):
  a, b = map(int, input().split())
  L.append((a,b))
L.sort()
DP_1 = [0]*N
DP_2 = [0]*(N+1)
DP_1[0], DP_2[1] = 1, 1
mod = 998244353
for i in range(1, N):
  for l in L:
    if l[0]>i:
      break
    elif l[1]>i:
      DP_1[i] += DP_2[i-l[0]+1]
      DP_1[i] %= mod
    elif l[1]<=i:
      DP_1[i] += DP_2[i-l[0]+1]-DP_2[i-l[1]]
      DP_1[i] %= mod
  DP_2[i+1] = DP_2[i] + DP_1[i]
  DP_2[i+1] %= mod
print(DP_1[-1]%mod)