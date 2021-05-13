import math
def combination(n,r):
      return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N = int(input())
A = list(map(int,input().split()))
ls = [0 for i in range(N)]
for i in range(N):
  ls[A[i]-1] += 1
summation = 0
for i in range(N):
  if ls[i] >= 2:
    summation += combination(ls[i],2)
for i in range(N):
  if ls[A[i]-1] >= 2:
    print(summation - (ls[A[i]-1] -1))
  else:
    print(summation)