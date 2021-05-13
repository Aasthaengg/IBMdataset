def solve():
  N, M = map(int, input().split())
  ans = [0]*N
  A = [0]*N
  B = [0]*N
  for i in range(N):
    A[i],B[i] = map(int, input().split())
  X = [0]*M
  Y = [0]*M
  for i in range(M):
    X[i],Y[i] = map(int, input().split())
  for i in range(N):
    ind = -1
    d_min = float('inf')
    for j in range(M):
      d = abs(A[i]-X[j])+abs(B[i]-Y[j])
      if d<d_min:
        d_min = d
        ind = j+1
    ans[i] = ind
  return ans
print(*solve(),sep='\n')