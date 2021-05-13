N = int(input())
A = list(map(int,input().split()))
M = 1000
S = 0
for i in range(N-1):
  M+=S*A[i]
  S = 0
  if A[i+1]>=A[i]:
    tmp=M//A[i]
    M -= tmp*A[i]
    S+=tmp
M+=S*A[-1]
S = 0
print(M)

