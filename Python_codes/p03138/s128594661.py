import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
m = math.ceil(math.log2(max(max(A),K)))+1
C = []
F = []
X = 0
for j in range(m):
  cnt = 0
  for i in range(N):
    cnt += A[i]>>j & 1
  if (N-cnt) < cnt:
    F.append(0)
  else:
    F.append(1)
    X += 2**j
  C.append(N-cnt)
ans = 0
for i in range(m-1,-1,-1):
  KK = K>>i & 1
  XX = X>>i & 1
  if KK==0 and XX==1:
    X += -2**i
    F[i]=0
  elif KK==1 and XX==0:
    break
  else:
    continue
for i in range(m-1,-1,-1):
  ans += C[i]*F[i]*(2**i)+(N-C[i])*(1-F[i])*(2**i)
print(ans)