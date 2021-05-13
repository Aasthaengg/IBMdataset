n = int(input())
q, r = divmod(n, 11)
if r == 0:
  print(q*2)
elif r <= 6:
  print(q*2 + 1)
else:
  print(q*2 + 2)