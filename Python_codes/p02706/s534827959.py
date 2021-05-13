N, M=map(int, input().split())
A = [int(i) for i in input().split()]

a = sum(A)

if N-a < 0:
  print(-1)
else:
  print(N-a)
