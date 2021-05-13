def kyuu(N):
  for i in range(8):
    if N >= 1800 - 200 * i:
      return (i + 1)
      break

X = int(input())
print(kyuu(X))