from collections import deque
def solve():
  N = int(input())
  A = list(map(int, input().split()))
  ans = deque([])
  for i in range(N):
    if i%2==0:
      ans.append(A[i])
    else:
      ans.appendleft(A[i])
  ans = list(ans)
  if N%2==1:
    ans = ans[::-1]
  return ans
print(*solve())