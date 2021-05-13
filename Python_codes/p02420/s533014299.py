while True:
  n = input()
  if n == "-":
    break
  m = int(input())
  for i in range(0, m):
    h = int(input())
    a = n[0:h]
    n = n[h:]
    n = n + a

  print(n)
