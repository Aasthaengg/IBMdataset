A, B, K = list(map(int, input().split()))

def exchange(a, b):
  if a % 2 == 1:
    a -= 1
  half = a/2
  return (half, b+half)

for i in range(K):
  if i % 2 == 0:
    A, B = exchange(A, B)
  else:
    B, A = exchange(B, A)

print(int(A), int(B))