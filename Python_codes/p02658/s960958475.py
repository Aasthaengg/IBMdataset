N = int(input())
A = list(map(int, input().split()))
if A.count(0)>0:
  print(0)
else:
  ans = A[0]
  for i in range(N-1):
    ans *= A[i+1]
    if ans > 10**18:
      print('-1')
      exit()
  print(ans)
