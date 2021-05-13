K, *A = map(int, open(0).read().split())
if A[-1]!=2:
  print(-1)
  import sys
  sys.exit()
S = 2
M = 2
for i in range(K-1,0,-1):
  c = A[i]
  p = A[i-1]
  ms = S
  mm = M+c-1
  ns = ms//p+1 if ms%p!=0 else ms//p
  nm = mm//p
  if ns*p>mm or nm*p<ms:
    print(-1)
    break
  M = nm*p
  S = ns*p
else:
  print(S,M+A[0]-1)