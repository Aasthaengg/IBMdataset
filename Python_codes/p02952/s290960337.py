N = int(input())

if N <= 9:
  print(N)
elif N <= 99:
  print(9)
elif N <= 999:
  print(9+(N-99))
elif N <= 9999:
  print(909)
elif N <= 99999:
  print(909+(N-9999))
elif N == 100000:
  print(90909)