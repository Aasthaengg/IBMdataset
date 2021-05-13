N = int(input())
A = []
for i in range(5):
  A.append(int(input()))
m = min(A)
print(4 + (N + m - 1) // m)