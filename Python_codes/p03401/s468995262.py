N = int(input())
A = list(map(int, input().split()))
A = [0] + A + [0]
S = 0
for i in range(1,N+2):
  S += abs(A[i]-A[i-1])
Si = [0]*(N+2)
for i in range(1, N+1):
  Si[i] = S-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1])
  print(Si[i])