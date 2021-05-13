def solve():
  N, P = map(int, input().split())
  A = list(map(int, input().split()))
  zero,one = 0,0
  for i in range(N):
    if A[i]%2==0:
      zero += 1
    else:
      one += 1
  ans = pow(2,N-1)
  if P==1 and one == 0:
    return 0
  if P==0 and one == 0:
    return pow(2,N)
  return ans
print(solve())