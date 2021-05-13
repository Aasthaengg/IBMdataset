import bisect

N, K = map(int, input().split())
Xs = list(map(int, input().split()))

rlt = float('inf')
i = bisect.bisect_left(Xs, 0)
if i-K >= 0:
  rlt = abs(Xs[i-K])

for j in range(i, i+K-1):
  if j >= N:
    break
  if j - K + 1 < 0:
    continue
  rlt = min(rlt, 2*abs(Xs[j-K+1])+Xs[j], abs(Xs[j-K+1])+2*Xs[j])
  
if i + K - 1 < N:
  rlt = min(rlt, Xs[i+K-1])
  
print(rlt)