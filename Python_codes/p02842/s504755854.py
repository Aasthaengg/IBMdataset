N = int(input())

for i in range(1, N + 1):
  if int(1.08 * i) == N:
    print(i)
    break
else:
  print(":(")
