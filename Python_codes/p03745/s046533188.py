import sys
sys.setrecursionlimit(1000000)
N = int(input())
A = list(map(int, input().split()))

ans = 0
def main(i, A):
  global N
  global ans
  if A[i] == A[i+1]:
    if i == N-2:
      ans += 1
      return ans
    else:
      return main(i+1, A)
  elif A[i] < A[i+1]:
    while i < N-1:
      if A[i] <= A[i+1]:
        i += 1
      else:
        ans += 1
        if i == N-2:
          ans += 1
          return ans
        else:
          return main(i+1, A)
    else:
      ans += 1
      return ans
  else:
    while i < N-1:
      if A[i] >= A[i+1]:
        i += 1
      else:
        ans += 1
        if i == N-2:
          ans += 1
          return ans
        else:
          return main(i+1, A)
    else:
      ans += 1
      return ans
    
if N == 1:
  print(1)
else:
  print(main(0, A))