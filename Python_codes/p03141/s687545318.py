def solve():
  ans = 0
  N = int(input())
  A = []
  for i in range(N):
    x,y = map(int, input().split())
    A.append([x+y,x,y])
  A.sort(reverse=True)
  for i in range(N):
    if i%2==0:
      ans += A[i][1]
    else:
      ans -= A[i][2]
  return ans
print(solve())