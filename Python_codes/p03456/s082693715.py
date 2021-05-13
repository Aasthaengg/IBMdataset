A = input().split()

X = int("".join(A))

found = 0
for i in range(1, 4000):
  if X // i == i and X % i == 0:
    found = 1
    break

if found:
  print("Yes")
else:
  print("No")