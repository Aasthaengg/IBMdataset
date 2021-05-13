N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if K >= N:
  cost = N*X
  print(cost)
elif K < N:
  cost = K*X + (N-K)*Y
  print(cost)
