N = int(input())
if len(str(N)) == 1:
  print(N)
elif len(str(N)) == 2:
  print(9)
elif len(str(N)) == 3:
  N = N - 90
  print(N)
elif len(str(N)) == 4:
  print(909)
elif len(str(N)) == 5:
  N = N - 9090
  print(N)
else:
  print(90909)