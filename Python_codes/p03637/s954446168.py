N = int(input())
A = list(map(int, input().split()))
X = [0, 0, 0]
for a in A:
  if a % 2 == 1:
    X[0] += 1
  elif a % 4 == 2:
    X[1] += 1
  else:
    X[2] += 1
if X[1] == 0:
  if X[2] >= X[0] - 1:
    print("Yes")
  else:
    print("No")
else:
  if X[2] >= X[0]:
    print("Yes")
  else:
    print("No")