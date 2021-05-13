N = int(input())
B = list(map(int,input().split()))
A = N*[0]

for n in range(N-1):
  if n==0:
    A[n]=B[n]
  else:
    A[n] = min(B[n-1],B[n])

print(sum(A)+B[-1])