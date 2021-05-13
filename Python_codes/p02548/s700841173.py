N = int(input())
s = 0
for i in range(1, N):
  b = (N - 1) // i
  s += b
print(s)
