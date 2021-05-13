N, M = map(int, input().split())
A = list(map(int, input().split()))
c = 0
s = sum(A)
for a in A:
  if a * 4 * M >= s:
    c += 1
if c >= M:
  print("Yes")
else:
  print("No")