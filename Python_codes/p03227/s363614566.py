from sys import stdin
S = stdin.readline().rstrip()
if len(S) == 2:
  print(S)
else:
  print(S[::-1])