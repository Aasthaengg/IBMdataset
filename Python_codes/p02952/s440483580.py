N = int(input())
if N < 100:
  print(min(9, N))
elif N < 10000:
  print(9 + min(N, 999) - 99)
else:
  print(9 + 900 + min(N, 99999) - 9999)