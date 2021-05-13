from itertools import accumulate
import sys
N,*L = map(int, open(0).read().split())
MOD = 10**9+7
T = L[:N]
A = L[N:]
h = [0]*N
p = -1
for i in range(N):
  if p != T[i]:
    p = T[i]
    h[i] = T[i]
p = -1
for i in range(N-1,-1,-1):
  if p!=A[i]:
    if h[i]!=0 and h[i]!=A[i]:
      print(0)
      sys.exit()
    p = A[i]
    h[i] = A[i]
xt = list(accumulate(h,max))
xa = list(accumulate(h[::-1],max))[::-1]
if xt!=T or xa!=A:
  print(0)
  sys.exit()
B = [min(t,a) for t,a in zip(T,A)]
ans = 1
for i in range(N):
  if h[i]==0:
    ans *= B[i]
    ans %= MOD
print(ans)