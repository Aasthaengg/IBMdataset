def abc048_c():
  n, x = map(int, input().split())
  A = list(map(int, input().split()))
  ans = 0
  B = []
  if A[0] > x:
    ans += A[0] - x
    B.append(x)
  else:
    B.append(A[0])
  for i in range(1, n):
    tmp = B[-1] + A[i]
    if tmp > x:
      ans += tmp - x
      B.append(x - B[-1])
    else:
      B.append(A[i])
  print(ans)

abc048_c()