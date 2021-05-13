N, K = map(int, input().split())
res = 0
for b in range(1, N+1):
  if K:
    res += (N//b) * max(0, b-K) + max(0, (N%b)-K+1) 
  else:
    res += (N//b) * max(0, b-K) + max(0, (N%b)-K+1) - 1

print(res)