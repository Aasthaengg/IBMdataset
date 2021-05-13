a, b = input().split()
na, nb = map(int, input().split())
c = input()
if a == c:
  print(na - 1, nb)
else:
  print(na, nb - 1)