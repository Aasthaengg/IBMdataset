N = int(input())
A = list(map(int, input().split()))
if N%2==0:
  B = [A[i] for i in range(N) if i%2==0]
  C = [A[(N-i-1)] for i in range(N) if (N-i-1)%2==1]
  print(*C+B)
else:
  B = [A[i] for i in range(N) if i%2==1]
  C = [A[(N-i-1)] for i in range(N) if (N-i-1)%2==0]
  print(*C+B)