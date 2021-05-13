def collatz(n):
  if n % 2 == 0:
    return int(n/2)
  else:
    return 3 * n + 1

A = [int(input())]
i = 1
while True:
  x = collatz(A[-1])
  if x in A:
    print(i + 1)
    break
  else:
    A.append(x)
    i += 1

