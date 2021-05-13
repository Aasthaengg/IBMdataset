N = int(input())
A = list(map(int,input().split()))
M = 1000
S = 0

for i in range(0, N):
  if i != N-1 and A[i] < A[i+1]:
    if S == 0:
      S = M // A[i]
      M = M % A[i]
  elif i == N-1 or A[i] > A[i+1]:
    if S > 0:
      M += S * A[i]
      S = 0  
print(M)