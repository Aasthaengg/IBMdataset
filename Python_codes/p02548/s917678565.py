N = int(input())
res = 0
for A in range(1, N + 1):
  res += (N - 1) // A
print(res)