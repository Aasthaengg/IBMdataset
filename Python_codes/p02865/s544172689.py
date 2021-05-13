N = int(input())

if N == 0:
  print(0)
elif N % 2 == 0:
  print(N//2-1)
else:
  print(N//2)