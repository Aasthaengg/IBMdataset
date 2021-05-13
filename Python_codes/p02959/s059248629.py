N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

count = 0
for i in range(N-1,-1,-1):
  n = min(A[i+1],B[i])
  A[i+1] -= n
  B[i] -= n
  count += n
  m = min(A[i],B[i])
  A[i] -= m
  B[i] -= m
  count += m

print(count)