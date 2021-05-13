N = int(input())
if 1 <= N < 10:
  print(N)
elif 10 <= N < 100:
  print(9)
elif 100 <= N < 1000:
  print(9 + N - 99)
elif 1000 <= N < 10000:
  print(909)
elif 10000 <= N < 100000:
  print(N - 9999 + 909)
elif N == 100000:
  print(90909)