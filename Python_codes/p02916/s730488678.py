N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
S = sum(B[A[i]-1] for i in range(N))
for i in range(N-1):
  if A[i+1]-1==A[i]:
    S += C[A[i]-1]
print(S)