from numba import njit

@njit
def calc(A):
    B = [0] * len(A)
    for i in range(len(A)):
        B[max(0,i - A[i])] += 1
        if i + A[i] + 1 < len(A):
            B[i + A[i] + 1] -= 1
    for i in range(1,len(B)):
        B[i] = B[i - 1] + B[i]
    return B

@njit
def solve(N,K,A):
  
  for i in range(K):
    A = calc(A)
    if len(set(A)) == 1 and A[0] == N:
      break
  return A
  
import sys
readline=sys.stdin.readline
  
N,K = map(int,readline().split())
A = list(map(int,readline().split()))

ans = solve(N,K,A)
print(*ans)