import operator
from itertools import accumulate

def main():
  N = int(input())
  A = list(map(int, input().split()))
  A_sum = list(reversed(list(accumulate(reversed(A))))) + [0]
  B = [0] * (N+1)

  B[0] = 1 - A[0]
  d = A_sum[0] + B[0]
  if B[0] < 0:
    return -1
  for i in range(1, N+1):
    B[i] = min(B[i - 1] * 2 - A[i], A_sum[i+1])
    
    if B[i] < 0:
      return -1
    d += B[i]
  return d

print(main())