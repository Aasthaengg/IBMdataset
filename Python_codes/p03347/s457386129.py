import sys
read = sys.stdin.read

n = int(input())
A = list(map(int, read().split()))
if A[0] != 0:
  print(-1)
else:
  ans = 0
  A += [0]
  for i in range(n):
    if A[i+1] - A[i] > 1:
      print(-1)
      exit()
    if A[i]+1 != A[i+1]:
      ans += A[i]
  print(ans)