N, K = map(int, input().split())
A = [int(x) for x in input().split()]

for i in range(N-K):
  t = A[i+K]/A[i]
  if t > 1:
    print("Yes")
  else:
    print("No")

