def easyLinearProgramming():
  A, B, C, K = map(int, input().split())
  if K <= A:
    print(K)
    return
  if K <= A + B:
    print(A)
    return
  print(2 * A + B - K)

easyLinearProgramming()