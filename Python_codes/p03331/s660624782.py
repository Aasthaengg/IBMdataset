N = int(input())
if N % 10 == 0:
  print(10)
else:
  ls = list(str(N))
  for i in range(len(ls)):
    ls[i] = int(ls[i])
  print(sum(ls))