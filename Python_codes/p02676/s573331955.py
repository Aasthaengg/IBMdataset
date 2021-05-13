K = int(input())
S = input()

if len(S) <= K:
  print(S)
else:
  S2 = S[:-(len(S) - K)] + "..."
  print(S2)