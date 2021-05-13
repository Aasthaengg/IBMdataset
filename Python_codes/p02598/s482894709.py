def check(N,target,A,K):
  cnt = 0
  for i in range(N):
    cnt += -(-A[i]//target)-1
  if cnt>K:
    return False
  return True

def solve():
  ans = 0
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  low = 1
  high = 10**9+1
  mid = (low+high)//2
  while high>low+1:
    if check(N,mid,A,K):
      high = mid
    else:
      low = mid
    mid = (low+high)//2
  if check(N,low,A,K):
    ans = low
  else:
    ans = high
  return ans
print(solve())
