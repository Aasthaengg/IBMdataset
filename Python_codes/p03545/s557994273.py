def si(p):
  if p == 0:
    return "-"
  else:
    return "+"
N = int(input())
X = [N // 1000, (N % 1000) // 100, (N % 100) // 10, N % 10]
f = 0
for i in range(2):
  for j in range(2):
    for k in range(2):
      x = X[0] + (2 * i - 1) * X[1] + (2 * j - 1) * X[2] + (2 * k - 1) * X[3]
      if x == 7:
        print(str(X[0]) + si(i) + str(X[1]) + si(j) + str(X[2]) + si(k) + str(X[3]) + "=7")
        f = 1
        break
    if f == 1:
      break
  if f == 1:
    break