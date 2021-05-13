N, M = map(int, input().split())
A = list(map(int, input().split()))
if sorted(A)[-M] >= sum(A) / (4*M):
  print("Yes")
else:
  print("No")