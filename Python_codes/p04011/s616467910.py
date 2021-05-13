N = int(input())
K = int(input())
x = int(input())
y = int(input())

if N <= K:
  print(N*x)
else:
  print(K*x + (N-K)*y)