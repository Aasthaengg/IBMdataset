A, B, K = map(int, input().split())

a = []
for i in range(1, min(A, B)+1):
  if A%i == 0 and B%i == 0:
    a.append(i)
b = sorted(a, reverse=True)
print(b[K-1])