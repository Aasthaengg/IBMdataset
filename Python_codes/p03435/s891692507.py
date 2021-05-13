A = list(map(int, input().split()))
x = A[1] - A[0]
y = A[2] - A[1]
f = 0
for i in range(2):
  B = list(map(int, input().split()))
  if B[1] - B[0] != x or B[2] - B[1] != y:
    f = 1
    break
if f == 0:
  print("Yes")
else:
  print("No")