N = int(input())

if N < 100:
  print(min(N,9))
elif N < 10000:
  print(min(N - 90, 909))
elif N < 1000000:
  print(min(N - 9090, 90909))
