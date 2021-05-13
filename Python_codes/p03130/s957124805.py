A = [0]*5
for _ in range(3):
  a, b = map(int, input().split())
  A[a] += 1
  A[b] += 1

if max(A) < 3:
  print("YES")
else:
  print("NO")